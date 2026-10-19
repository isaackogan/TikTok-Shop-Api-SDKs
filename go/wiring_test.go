package tiktokshop

import (
	"encoding/json"
	"os"
	"reflect"
	"sort"
	"strings"
	"testing"

	"github.com/isaackogan/TikTok-Shop-Api-SDKs/go/generated"
)

// goGroupName is the PascalCase form of a canonical group name (ruling R9: "TikTok" is one word,
// which camelCase and PascalCase already keep together).
func goGroupName(g string) string { return strings.ToUpper(g[:1]) + g[1:] }

func TestGroupNames(t *testing.T) {
	raw, err := os.ReadFile("../shared/api-groups.json")
	if err != nil {
		t.Fatal(err)
	}
	var tags map[string]string
	if err := json.Unmarshal(raw, &tags); err != nil {
		t.Fatal(err)
	}
	var want []string
	for _, g := range tags {
		want = append(want, goGroupName(g))
	}
	sort.Strings(want)
	explicit := []string{
		"AffiliateCreator", "AffiliatePartner", "AffiliateSeller", "Analytics", "Authorization",
		"CustomerEngagement", "CustomerService", "Event", "Finance", "FulfilledByTikTok", "Fulfillment",
		"Logistics", "Orders", "Products", "Promotion", "ReturnAndRefund", "Seller", "SupplyChain", "Tools",
	}
	if !reflect.DeepEqual(want, explicit) {
		t.Fatalf("api-groups.json gives %v, want %v", want, explicit)
	}
	// Every exported *APIService field of TikTokShop, and nothing else of that shape.
	var got []string
	rt := reflect.TypeOf(TikTokShop{})
	for i := 0; i < rt.NumField(); i++ {
		f := rt.Field(i)
		if f.IsExported() {
			got = append(got, f.Name)
		}
	}
	sort.Strings(got)
	if !reflect.DeepEqual(got, explicit) {
		t.Errorf("TikTokShop exported fields = %v, want %v", got, explicit)
	}
}

func TestEveryOperationIsAMethodOnItsGroup(t *testing.T) {
	if len(generated.Operations) != 320 {
		t.Errorf("operations = %d, want 320", len(generated.Operations))
	}
	shop := reflect.ValueOf(New(Options{AppKey: "k", AppSecret: "s"})).Elem()
	for _, op := range generated.Operations {
		field := shop.FieldByName(goGroupName(op.Group))
		if !field.IsValid() {
			t.Errorf("%s: no field %s", op.OperationID, goGroupName(op.Group))
			continue
		}
		// A concrete generated service, never an interface.
		ft := field.Type()
		if ft.Kind() != reflect.Pointer || ft.Elem().Name() != op.Service || ft.Elem().PkgPath() != reflect.TypeOf(generated.APIClient{}).PkgPath() {
			t.Errorf("%s: field type %v, want *generated.%s", op.OperationID, ft, op.Service)
			continue
		}
		if field.IsNil() {
			t.Errorf("%s: service is nil", op.OperationID)
			continue
		}
		if _, ok := ft.MethodByName(op.Method); !ok {
			t.Errorf("%s: %s has no method %s", op.OperationID, ft, op.Method)
		}
	}
}
