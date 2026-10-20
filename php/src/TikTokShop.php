<?php

declare(strict_types=1);

namespace TikTokShop\Api;

use GuzzleHttp\Client;
use GuzzleHttp\ClientInterface;
use TikTokShop\Api\Generated;

/**
 * The TikTok Shop API client: one public property per API group, each the generated `*Api` class for that tag.
 *
 * Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
 *
 * ```php
 * $shop = new TikTokShop(appKey: '...', appSecret: '...', accessToken: '...', shopCipher: '...');
 * $shops = $shop->authorization->getAuthorizedShops();
 * ```
 *
 * Every request is signed, and every failure is a {@see TikTokShopException}. The generated methods take their
 * parameters positionally, in the order of the generated signature.
 *
 * HTTP client: by default the SDK builds a Guzzle client that never follows redirects (a 3xx reply is thrown as a
 * {@see TikTokShopException} with code 302 and the redirect target receives nothing), with the given timeout, and
 * with Guzzle's default proxy behaviour. A client you pass as `$httpClient` is used as is, so its own redirect,
 * timeout and proxy settings apply and `$timeout` is ignored.
 */
final class TikTokShop
{
    public const DEFAULT_BASE_URL = 'https://open-api.tiktokglobalshop.com';

    /** Seconds, used when no `$timeout` is given. */
    public const DEFAULT_TIMEOUT = 30.0;

    /**
     * The version {@see self::userAgent()} reports when Composer cannot tell (a checkout rather than an install).
     * `scripts/bump-version.ts` keeps it in step with the release tag.
     */
    private const VERSION = '0.1.0';

    private const PACKAGE = 'isaackogan/tiktok-shop-api';

    public readonly Generated\Api\AffiliateCreatorApi $affiliateCreator;
    public readonly Generated\Api\AffiliatePartnerApi $affiliatePartner;
    public readonly Generated\Api\AffiliateSellerApi $affiliateSeller;
    public readonly Generated\Api\AnalyticsApi $analytics;
    public readonly Generated\Api\AuthorizationApi $authorization;
    public readonly Generated\Api\CustomerEngagementApi $customerEngagement;
    public readonly Generated\Api\CustomerServiceApi $customerService;
    public readonly Generated\Api\EventApi $event;
    public readonly Generated\Api\FinanceApi $finance;
    public readonly Generated\Api\FulfilledByTikTokFBTApi $fulfilledByTikTok;
    public readonly Generated\Api\FulfillmentApi $fulfillment;
    public readonly Generated\Api\LogisticsApi $logistics;
    public readonly Generated\Api\OrdersApi $orders;
    public readonly Generated\Api\ProductsApi $products;
    public readonly Generated\Api\PromotionApi $promotion;
    public readonly Generated\Api\ReturnAndRefundApi $returnAndRefund;
    public readonly Generated\Api\SellerApi $seller;
    public readonly Generated\Api\SupplyChainApi $supplyChain;
    public readonly Generated\Api\ToolsApi $tools;

    private readonly Credentials $credentials;

    private readonly ClientInterface $httpClient;

    private readonly string $baseUrl;

    /**
     * @param string|null $accessToken Sent as `x-tts-access-token`.
     * @param string|null $shopCipher Added as `shop_cipher` to the operations that take one.
     * @param string|null $baseUrl Defaults to {@see self::DEFAULT_BASE_URL}.
     * @param float|null $timeout Seconds for the whole request, for the client the SDK builds. 0 means no limit.
     *                            Defaults to {@see self::DEFAULT_TIMEOUT}.
     * @param ClientInterface|null $httpClient A Guzzle client to use as is, see the class comment.
     */
    public function __construct(
        string $appKey,
        string $appSecret,
        ?string $accessToken = null,
        ?string $shopCipher = null,
        ?string $baseUrl = null,
        ?float $timeout = null,
        ?ClientInterface $httpClient = null,
    ) {
        if ($timeout !== null && $timeout < 0) {
            throw new \InvalidArgumentException('timeout must not be negative (0 means no limit)');
        }
        $this->baseUrl = rtrim($baseUrl ?? self::DEFAULT_BASE_URL, '/');
        $this->credentials = new Credentials($appKey, $appSecret, $accessToken, $shopCipher);
        $this->httpClient = $httpClient ?? new Client([
            'allow_redirects' => false,
            'http_errors' => false,
            'timeout' => $timeout ?? self::DEFAULT_TIMEOUT,
            'connect_timeout' => $timeout ?? self::DEFAULT_TIMEOUT,
        ]);

        $signing = new SigningClient($this->httpClient, $this->credentials);
        $config = (new Generated\Configuration())->setHost($this->baseUrl)->setUserAgent(self::userAgent());
        $this->affiliateCreator = new Generated\Api\AffiliateCreatorApi($signing, $config);
        $this->affiliatePartner = new Generated\Api\AffiliatePartnerApi($signing, $config);
        $this->affiliateSeller = new Generated\Api\AffiliateSellerApi($signing, $config);
        $this->analytics = new Generated\Api\AnalyticsApi($signing, $config);
        $this->authorization = new Generated\Api\AuthorizationApi($signing, $config);
        $this->customerEngagement = new Generated\Api\CustomerEngagementApi($signing, $config);
        $this->customerService = new Generated\Api\CustomerServiceApi($signing, $config);
        $this->event = new Generated\Api\EventApi($signing, $config);
        $this->finance = new Generated\Api\FinanceApi($signing, $config);
        $this->fulfilledByTikTok = new Generated\Api\FulfilledByTikTokFBTApi($signing, $config);
        $this->fulfillment = new Generated\Api\FulfillmentApi($signing, $config);
        $this->logistics = new Generated\Api\LogisticsApi($signing, $config);
        $this->orders = new Generated\Api\OrdersApi($signing, $config);
        $this->products = new Generated\Api\ProductsApi($signing, $config);
        $this->promotion = new Generated\Api\PromotionApi($signing, $config);
        $this->returnAndRefund = new Generated\Api\ReturnAndRefundApi($signing, $config);
        $this->seller = new Generated\Api\SellerApi($signing, $config);
        $this->supplyChain = new Generated\Api\SupplyChainApi($signing, $config);
        $this->tools = new Generated\Api\ToolsApi($signing, $config);
    }

    /**
     * The User-Agent of every API and token call: `tiktok-shop-api-php/<version>`. The version is the installed package's,
     * as Composer records it, so a release reports its own tag (the Packagist mirror is pushed before the release commit
     * stamps {@see self::VERSION}).
     */
    public static function userAgent(): string
    {
        $version = self::VERSION;
        if (class_exists(\Composer\InstalledVersions::class) && \Composer\InstalledVersions::isInstalled(self::PACKAGE)) {
            $pretty = \Composer\InstalledVersions::getPrettyVersion(self::PACKAGE);
            if (is_string($pretty) && preg_match('/^v?(\d+\.\d+\.\d+)$/', $pretty, $m) === 1) {
                $version = $m[1];
            }
        }

        return 'tiktok-shop-api-php/' . $version;
    }

    /**
     * A client for another shop or token that shares this client's HTTP client. This client is not changed.
     *
     * An argument you leave out keeps this client's value ({@see Keep::Current}); `null` or `''` clears it.
     */
    public function withShop(string|null|Keep $accessToken = Keep::Current, string|null|Keep $shopCipher = Keep::Current): self
    {
        $next = $this->credentials->with($accessToken, $shopCipher);

        return new self(
            appKey: $next->appKey,
            appSecret: $next->appSecret(),
            accessToken: $next->accessToken(),
            shopCipher: $next->shopCipher(),
            baseUrl: $this->baseUrl,
            httpClient: $this->httpClient,
        );
    }

    /** @return array<string, mixed> */
    public function __debugInfo(): array
    {
        return [
            'baseUrl' => $this->baseUrl,
            'credentials' => $this->credentials,
        ];
    }
}
