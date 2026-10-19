package tiktokshop

import "fmt"

// Error is returned (wrapped in a *url.Error by net/http) for every failed call. See the package
// documentation for the failure classes.
type Error struct {
	// Code is the TikTok error code. For a non-2xx response without one it is the HTTP status; it is 0
	// for a response that is not JSON and for network errors.
	Code int
	// Message is TikTok's message, or a description of what went wrong.
	Message string
	// RequestID is TikTok's request_id, empty when the response had none.
	RequestID string
	// HTTPStatus is the response status, 0 when no response arrived.
	HTTPStatus int
	// Cause is the underlying error (a parse error, a network error, a context error), if any.
	Cause error
}

func (e *Error) Error() string {
	s := "tiktokshop: " + e.Message
	if e.Code != 0 {
		s += fmt.Sprintf(" (code %d", e.Code)
		if e.RequestID != "" {
			s += ", request_id " + e.RequestID
		}
		s += ")"
	} else if e.RequestID != "" {
		s += fmt.Sprintf(" (request_id %s)", e.RequestID)
	}
	return s
}

// Unwrap returns the underlying error, so errors.Is and errors.As see through an Error.
func (e *Error) Unwrap() error { return e.Cause }
