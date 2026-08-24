# Olist E-Commerce Data Cleaning & Merge

A larger-scale data cleaning project using the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — 9 linked CSV files covering ~100k orders (2016–2018). Goal: clean and merge multiple related tables into one working dataset to analyze whether **review scores correlate with delivery time, and whether that relationship varies by product category**.

Unlike the single-file workout project, this dataset required understanding relationships between tables (primary/foreign keys) before merging, not just cleaning one flat file.

## Files Used

| File | Role |
|---|---|
| `olist_orders_dataset.csv` | Base table — order dates, status |
| `olist_customers_dataset.csv` | Customer location info |
| `olist_order_items_dataset.csv` | Products/items per order |
| `olist_order_payments_dataset.csv` | Payment method(s) per order |
| `olist_order_reviews_dataset.csv` | Review score + comments |
| `olist_products_dataset.csv` | Product details |
| `olist_sellers_dataset.csv` | Seller info |
| `product_category_name_translation.csv` | Portuguese → English category names |
| `olist_geolocation_dataset.csv` | Excluded — see note below |

## Cleaning Issues Found & Fixed

| Table | Issue | Fix |
|---|---|---|
| Customers | Zip codes stored as integers, silently dropping leading zeros (e.g. `05000` → `5000`) for São Paulo-state codes | Verified against city/state, then restored with `.str.zfill(5)` |
| Customers | 3,345 duplicate `customer_unique_id` values | Not dropped — confirmed these are repeat customers with multiple orders (`customer_id` is order-level, `customer_unique_id` is person-level) |
| Geolocation | Garbled city name encoding (e.g. `ParabÃ©ns` / broken accented characters) | Cleaned via targeted character replacement; verified fix against original values with no unintended changes |
| Order Items | `order_id` appears multiple times | Not a bug — orders with multiple items have one row per item. Verified using `order_id` + `order_item_id` combined uniqueness, which came back clean |
| Order Reviews | 58,247 missing `review_comment_message` / 87,656 missing `review_comment_title` | Expected — comments are optional. Filled with an explicit placeholder (`"No review submitted"`) rather than dropping rows, since `review_score` is still valid without a comment |
| Order Reviews | 814 duplicate `review_id` values | Investigated before deciding: checked whether duplicates shared the same `order_id` (true duplicate) or differed (one review linked to multiple orders) before choosing a fix |

## Merging

Merged step-by-step (not all at once) through the following chain, checking row count after each join to catch unexpected duplication early:

```
orders → customers → order_items → order_payments → order_reviews → products → sellers
```

| Step | Row count |
|---|---|
| orders (base) | 99,441 |
| + customers | 99,441 |
| + order_items | 113,425 |
| + order_payments | 118,434 |
| + order_reviews | 118,763 |
| + products | 118,763 |
| + sellers | 118,763 |

Row count growth after `order_items` and `order_payments` is expected (orders can have multiple items or split payments). No unexpected spikes.

**Geolocation was intentionally excluded** from the merge. Both `customer_zip_code_prefix` and `geolocation_zip_code_prefix` are non-unique on their respective sides, making it a many-to-many join — merging it caused row count to explode into the millions with no analytical benefit for this project's question.

## Tools

Python, pandas

## Next Steps

Calculate delivery time per order and analyze its relationship to review score, broken down by product category.