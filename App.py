import streamlit as st
import pandas as pd

# Sample data for products and sales
products_data = {
    "Product ID": [1, 2, 3],
    "Product Name": ["Lipstick", "Foundation", "Mascara"],
    "Price": [20.0, 30.0, 15.0],
    "Stock": [100, 150, 200]
}

sales_data = {
    "Sale ID": [1, 2, 3],
    "Product ID": [1, 2, 3],
    "Quantity Sold": [10, 5, 20],
    "Total Revenue": [200.0, 150.0, 300.0]
}

feedback_data = {
    "Feedback ID": [1, 2, 3],
    "Product Name": ["Lipstick", "Foundation", "Mascara"],
    "Rating": [5, 4, 3],
    "Comment": ["Loved it!", "Good coverage", "Okay but not great"]
}

# Create DataFrames
products_df = pd.DataFrame(products_data)
sales_df = pd.DataFrame(sales_data)
feedback_df = pd.DataFrame(feedback_data)

# Streamlit app layout
st.title("Angelina Cosmetics and Management App")

# Sidebar for navigation
st.sidebar.header("Navigation")
app_mode = st.sidebar.selectbox("Choose the app mode", ["Home", "Manage Products", "View Sales", "Customer Feedback"])

# Home page
if app_mode == "Home":
    st.subheader("Welcome to Angelina Cosmetics!")
    st.write("Manage your products, view sales data, and gather customer feedback.")

# Manage Products
elif app_mode == "Manage Products":
    st.subheader("Manage Products")
    
    # Product management section
    st.write("### Current Product Inventory")
    st.dataframe(products_df)

    st.write("### Add New Product")
    new_product_name = st.text_input("Product Name")
    new_product_price = st.number_input("Price", min_value=0.0, format="%.2f")
    new_product_stock = st.number_input("Stock", min_value=0)
    
    if st.button("Add Product"):
        new_id = products_df["Product ID"].max() + 1
        new_row = pd.DataFrame([[new_id, new_product_name, new_product_price, new_product_stock]], columns=products_df.columns)
        products_df = pd.concat([products_df, new_row], ignore_index=True)
        st.success(f"Product {new_product_name} added!")

    st.write("### Update Product Stock")
    product_id_to_update = st.number_input("Product ID to update", min_value=1)
    new_stock_value = st.number_input("New Stock Value", min_value=0)

    if st.button("Update Stock"):
        if product_id_to_update in products_df["Product ID"].values:
            products_df.loc[products_df["Product ID"] == product_id_to_update, "Stock"] = new_stock_value
            st.success(f"Updated stock for Product ID {product_id_to_update}!")
        else:
            st.error("Product ID not found!")

# View Sales
elif app_mode == "View Sales":
    st.subheader("Sales Overview")
    
    st.write("### Current Sales Data")
    st.dataframe(sales_df)

    st.write("### Total Revenue")
    total_revenue = sales_df["Total Revenue"].sum()
    st.write(f"Total Revenue: ${total_revenue:.2f}")

# Customer Feedback
elif app_mode == "Customer Feedback":
    st.subheader("Customer Feedback")
    
    st.write("### Feedback Overview")
    st.dataframe(feedback_df)

    st.write("### Submit Feedback")
    feedback_product_name = st.selectbox("Select Product", products_df["Product Name"])
    feedback_rating = st.slider("Rating", 1, 5)
    feedback_comment = st.text_area("Comment")

    if st.button("Submit Feedback"):
        new_feedback_id = feedback_df["Feedback ID"].max() + 1
        new_feedback_row = pd.DataFrame([[new_feedback_id, feedback_product_name, feedback_rating, feedback_comment]], columns=feedback_df.columns)
        feedback_df = pd.concat([feedback_df, new_feedback_row], ignore_index=True)
        st.success("Feedback submitted successfully!")

# Display all sections in a simple structure
st.write("---")
st.sidebar.write("Developed by Angelina Cosmetics Team")
