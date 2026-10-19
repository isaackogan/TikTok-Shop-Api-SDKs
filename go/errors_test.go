package tiktokshop

import (
	"errors"
	"net/url"
	"testing"
)

func TestErrorUnwrapAndString(t *testing.T) {
	cause := errors.New("boom")
	e := &Error{Code: 5, Message: "bad", RequestID: "r", HTTPStatus: 500, Cause: cause}
	if !errors.Is(e, cause) {
		t.Error("Unwrap should expose the cause")
	}
	wrapped := &url.Error{Op: "Get", URL: "x", Err: e}
	var got *Error
	if !errors.As(wrapped, &got) || got != e {
		t.Error("errors.As through *url.Error failed")
	}
	if e.Error() == "" {
		t.Error("empty message")
	}
}
