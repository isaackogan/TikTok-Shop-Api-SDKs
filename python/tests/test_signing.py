import json
from pathlib import Path

import pytest

from tiktok_shop_api import Signer, operation_for, requires_shop_cipher

VECTORS = json.loads(
    (Path(__file__).resolve().parents[2] / "shared/test-vectors/signing.json").read_text(encoding="utf-8")
)["cases"]


def _req(c):
    return {
        "path": c["path"],
        "query": [tuple(p) for p in c["query"]],
        "content_type": c["contentType"],
        "body": None if c["body"] is None else c["body"].encode("utf-8"),
        "app_secret": c["secret"],
    }


def test_has_the_six_shared_cases():
    assert len(VECTORS) == 6


@pytest.mark.parametrize("case", VECTORS, ids=lambda c: c["name"])
def test_string_to_sign(case):
    assert Signer.string_to_sign(**_req(case)) == case["stringToSign"]


@pytest.mark.parametrize("case", VECTORS, ids=lambda c: c["name"])
def test_sign(case):
    assert Signer.sign(**_req(case)) == case["sign"]


def test_sign_accepts_str_body():
    c = VECTORS[1]
    assert Signer.sign(**{**_req(c), "body": c["body"]}) == c["sign"]


def test_post_search_needs_cipher():
    assert requires_shop_cipher("POST", "/order/202309/orders/search") is True


def test_method_is_case_insensitive():
    assert requires_shop_cipher("post", "/order/202309/orders/search") is True


def test_authorized_shops_does_not():
    assert requires_shop_cipher("GET", "/authorization/202309/shops") is False


def test_param_segment_matches_one_segment():
    assert requires_shop_cipher("GET", "/product/202309/products/1729507467923261408") is True
    assert requires_shop_cipher("GET", "/product/202309/products/1/2") is False


def test_unknown_path_is_false():
    assert requires_shop_cipher("GET", "/nope") is False


def test_operation_for_prefers_literal_segments():
    def op(m, p):
        o = operation_for(m, p)
        return o and o["operationId"]

    assert op("POST", "/product/202604/appeals/submit") == "submitSizeChartAppeal"
    assert op("DELETE", "/product/202604/appeals/submit") is None
    assert op("GET", "/product/202604/opportunities/submissions") == "getSubmissionRecords"
