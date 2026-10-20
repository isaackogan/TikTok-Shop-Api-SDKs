// Code in this file is copied verbatim from README.md, so the README compiles. TestREADMEMatchesExamples
// fails when a README line is missing here.

package tiktokshop_test

import (
	"context"
	"errors"
	"fmt"
	"io"
	"log"
	"net/http"

	tiktokshop "github.com/isaackogan/TikTok-Shop-Api-SDKs/go"
	"github.com/isaackogan/TikTok-Shop-Api-SDKs/go/generated"
)

func authorize(ctx context.Context) error {
	auth := tiktokshop.NewAuth(tiktokshop.AuthOptions{
		AppKey:    "APP_KEY",
		AppSecret: "APP_SECRET",
		ServiceID: "SERVICE_ID",
	})

	url, err := auth.AuthorizationURL(tiktokshop.AuthorizationURLOptions{
		Type:   tiktokshop.AuthSeller,
		Region: tiktokshop.RegionUS,
		State:  "my-csrf-token",
	})
	if err != nil {
		return err
	}
	fmt.Println("send the seller to", url)

	tokens, err := auth.ExchangeCode(ctx, "CODE_FROM_THE_REDIRECT")
	if err != nil {
		return err
	}
	fmt.Println(tokens.AccessToken, tokens.OpenID, tokens.GrantedScopes)

	tokens, err = auth.Refresh(ctx, tokens.RefreshToken)
	if err != nil {
		return err
	}
	fmt.Println("expires at", tokens.AccessTokenExpireIn)
	return nil
}

func listOrders(ctx context.Context) error {
	client := tiktokshop.New(tiktokshop.Options{
		AppKey:      "APP_KEY",
		AppSecret:   "APP_SECRET",
		AccessToken: "ACCESS_TOKEN",
		ShopCipher:  "SHOP_CIPHER",
	})

	orders, _, err := client.Orders.GetOrderList(ctx).PageSize(20).Execute()
	if err != nil {
		return err
	}
	data := orders.GetData()
	fmt.Println(data.GetTotalCount(), "orders; request", orders.GetRequestId())
	return nil
}

func handleErrors(ctx context.Context, client *tiktokshop.TikTokShop) {
	_, _, err := client.Orders.GetOrderList(ctx).Execute()

	var apiErr *tiktokshop.Error
	if errors.As(err, &apiErr) {
		fmt.Println(apiErr.Code, apiErr.Message, apiErr.RequestID, apiErr.HTTPStatus)
	}
}

func otherShop(client *tiktokshop.TikTokShop) *tiktokshop.TikTokShop {
	return client.WithShop(
		tiktokshop.ShopAccessToken("OTHER_ACCESS_TOKEN"),
		tiktokshop.ShopCipher("OTHER_SHOP_CIPHER"),
	)
}

func webhookHandler(w http.ResponseWriter, r *http.Request) {
	body, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "read failed", http.StatusBadRequest)
		return
	}

	event, err := tiktokshop.Webhooks.VerifyAndParse(tiktokshop.WebhookVerifyOptions{
		AppKey:    "APP_KEY",
		AppSecret: "APP_SECRET",
		RawBody:   body,
		Signature: r.Header.Get("Authorization"),
	})
	if errors.Is(err, tiktokshop.ErrWebhookSignature) {
		http.Error(w, "bad signature", http.StatusUnauthorized)
		return
	}
	if err != nil {
		http.Error(w, "bad webhook", http.StatusBadRequest)
		return
	}

	switch e := event.(type) {
	case *generated.OrderStatusChangeWebhook:
		log.Println("order", e.Data.GetOrderId(), "is now", e.Data.GetOrderStatus(), "in shop", e.GetShopId())
	case *generated.ReturnStatusChangeWebhook:
		log.Println("return", e.Data.GetReturnId())
	case tiktokshop.UnknownWebhookEvent:
		log.Println("unhandled webhook type", e.Type)
	}
	w.WriteHeader(http.StatusOK)
}
