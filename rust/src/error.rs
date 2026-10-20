//! The crate's error type.
use std::fmt;

use crate::generated::apis;

/// Everything that can go wrong with a call.
///
/// A failure that reached TikTok (an envelope with `code != 0`, a non-2xx status, a 2xx reply that is not
/// JSON) is [`Error::Api`]. Transport failures never carry the request URL, because the URL holds the
/// signature and other request parameters.
#[derive(Debug)]
#[non_exhaustive]
pub enum Error {
    /// TikTok answered with an error, or with something that is not an API reply.
    Api {
        /// TikTok's error code. For a non-2xx reply without one it is the HTTP status; it is `-1` for a 2xx
        /// reply that is not JSON.
        code: i64,
        /// TikTok's message, or a description of what went wrong.
        message: String,
        /// TikTok's `request_id`, empty when the reply had none.
        request_id: String,
        /// The HTTP status.
        http_status: Option<u16>,
    },
    /// A transport error (connection refused, DNS, TLS, ...). The URL is stripped.
    Http(reqwest::Error),
    /// The request exceeded the configured timeout.
    Timeout,
    /// A reply that is valid JSON but does not fit the expected model.
    Decode(serde_json::Error),
    /// Reading a file to upload failed.
    Io(std::io::Error),
    /// Anything else, as text.
    Other(String),
}

impl Error {
    /// The TikTok error code, when this is an [`Error::Api`].
    pub fn code(&self) -> Option<i64> {
        match self {
            Error::Api { code, .. } => Some(*code),
            _ => None,
        }
    }

    /// TikTok's `request_id`, when this is an [`Error::Api`] that has one.
    pub fn request_id(&self) -> Option<&str> {
        match self {
            Error::Api { request_id, .. } if !request_id.is_empty() => Some(request_id),
            _ => None,
        }
    }

    pub(crate) fn from_reqwest(e: reqwest::Error) -> Self {
        let e = e.without_url();
        if e.is_timeout() {
            Error::Timeout
        } else {
            Error::Http(e)
        }
    }
}

impl fmt::Display for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Error::Api { code, message, request_id, http_status } => {
                write!(f, "tiktok shop: {message} (code {code}")?;
                if !request_id.is_empty() {
                    write!(f, ", request_id {request_id}")?;
                }
                if let Some(s) = http_status {
                    write!(f, ", HTTP {s}")?;
                }
                write!(f, ")")
            }
            Error::Http(e) => write!(f, "tiktok shop: request failed: {e}"),
            Error::Timeout => write!(f, "tiktok shop: the request timed out"),
            Error::Decode(e) => write!(f, "tiktok shop: the reply does not match the expected model: {e}"),
            Error::Io(e) => write!(f, "tiktok shop: {e}"),
            Error::Other(m) => write!(f, "tiktok shop: {m}"),
        }
    }
}

impl std::error::Error for Error {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        match self {
            Error::Http(e) => Some(e),
            Error::Decode(e) => Some(e),
            Error::Io(e) => Some(e),
            _ => None,
        }
    }
}

impl From<reqwest_middleware::Error> for Error {
    fn from(e: reqwest_middleware::Error) -> Self {
        match e {
            reqwest_middleware::Error::Reqwest(e) => Error::from_reqwest(e),
            // The signing middleware reports TikTok's failures as this crate's Error.
            reqwest_middleware::Error::Middleware(e) => match e.downcast::<Error>() {
                Ok(ours) => ours,
                Err(other) => Error::Other(other.to_string()),
            },
        }
    }
}

impl<E> From<apis::Error<E>> for Error {
    fn from(e: apis::Error<E>) -> Self {
        match e {
            apis::Error::Reqwest(e) => Error::from_reqwest(e),
            apis::Error::ReqwestMiddleware(e) => e.into(),
            apis::Error::Serde(e) => Error::Decode(e),
            apis::Error::Io(e) => Error::Io(e),
            // The signing middleware turns every non-2xx reply into Error::Api first; this is a fallback.
            apis::Error::ResponseError(r) => Error::Api {
                code: i64::from(r.status.as_u16()),
                message: r.content,
                request_id: String::new(),
                http_status: Some(r.status.as_u16()),
            },
        }
    }
}
