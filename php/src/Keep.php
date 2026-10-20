<?php

declare(strict_types=1);

namespace TikTokShop\Api;

/**
 * The default of the optional arguments of {@see TikTokShop::withShop()}: keep this client's current value.
 * Pass `null` or `''` to clear a value instead.
 */
enum Keep
{
    case Current;
}
