//! An unofficial client for the TikTok Shop Partner API, generated from TikTok's documentation.
//!
//! Unofficial. Not affiliated with or endorsed by TikTok or ByteDance.
//!
//! [`TikTokShop`] has one field per API group (`client.orders`, `client.products`, ...); each method signs
//! its request and turns a failed reply into an [`Error`]. The models are in [`generated::models`].

pub mod client;
pub mod error;
pub mod generated;
pub mod signing;

pub use client::{Options, Shop, TikTokShop, DEFAULT_BASE_URL, DEFAULT_TIMEOUT};
pub use error::Error;
