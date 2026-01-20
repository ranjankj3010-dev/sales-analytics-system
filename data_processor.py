# To calculate total revenue

def calculate_total_revenue(transactions):
    total_revenue = 0.0
    for t in transactions:
        total_revenue += t["Quantity"] * t["UnitPrice"]
    return total_revenue


_______________________________________________________________________________________

def region_wise_sales(transactions):
    region_stats = {}
    total_sales_all = 0.0

    # Calculate total sales and transaction count per region
    for t in transactions:
        region = t["Region"]
        amount = t["Quantity"] * t["UnitPrice"]
        total_sales_all += amount

        if region not in region_stats:
            region_stats[region] = {
                "total_sales": 0.0,
                "transaction_count": 0
            }

        region_stats[region]["total_sales"] += amount
        region_stats[region]["transaction_count"] += 1

    # Calculate percentage of total sales
    for region in region_stats:
        region_stats[region]["percentage"] = (
            (region_stats[region]["total_sales"] / total_sales_all) * 100
            if total_sales_all > 0 else 0
        )

    # Sort by total_sales descending
    sorted_regions = dict(
        sorted(
            region_stats.items(),
            key=lambda item: item[1]["total_sales"],
            reverse=True
        )
    )

    return sorted_regions


_______________________________________________________________________________________

def top_selling_products(transactions, n=5):
    product_summary = {}

    for t in transactions:
        name = t["ProductName"]
        qty = t["Quantity"]
        revenue = t["Quantity"] * t["UnitPrice"]

        if name not in product_summary:
            product_summary[name] = {
                "total_quantity": 0,
                "total_revenue": 0.0
            }

        product_summary[name]["total_quantity"] += qty
        product_summary[name]["total_revenue"] += revenue

    # Sort by total quantity sold (descending)
    sorted_products = sorted(
        product_summary.items(),
        key=lambda x: x[1]["total_quantity"],
        reverse=True
    )

    # Return top n products
    return [
        (name, data["total_quantity"], data["total_revenue"])
        for name, data in sorted_products[:n]
    ]
