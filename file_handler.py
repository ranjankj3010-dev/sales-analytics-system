 def read_sales_data ("Sales - data.rtf""):
    encodings = ["utf-8", "latin-1", "cp1252"]

    for encoding in encodings:
        try:
            with open("Sales - data.rtf", "r", encoding=encoding) as file:
                lines = file.readlines()

            # Skip header and remove empty lines
            return [line.strip() for line in lines[1:] if line.strip()]

        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"Error: File not found -> {filename}")
            return []

    print("Error: Unable to read file with supported encodings.")
    return []

__________________________________________________________________________________________


def parse_transactions(raw_lines):
    parsed_data = []

    for line in raw_lines:
        parts = line.strip().split("|")

        if len(parts) != 8:
            continue

        transaction_id, date, product_id, product_name, quantity, unit_price, customer_id, region = parts

        product_name = product_name.replace(",", " ")

        try:
            quantity = int(quantity.replace(",", ""))
            unit_price = float(unit_price.replace(",", ""))
        except ValueError:
            continue

        parsed_data.append({
            "TransactionID": transaction_id,
            "Date": date,
            "ProductID": product_id,
            "ProductName": product_name,
            "Quantity": quantity,
            "UnitPrice": unit_price,
            "CustomerID": customer_id,
            "Region": region
        })

    return parsed_data

print(parse_transactions(raw_lines))


