import streamlit as st


st.title("Sales Force Commission Calculator")

# Step 1: Select Main Category
main_category = st.selectbox(
    "Select Main Category",
    ["JEFS Deal Become Paid"]
)

# Step 2: Select Subcategory (Initial JEFS Sold or Expansion for Existing JEFS)
subcategory = st.selectbox(
    "Select Subcategory",
    ["Initial JEFS Sold", "Expansion for Existing JEFS"]
)

# Step 3: Select Deal Type (Options Based on Subcategory)
deal_type_options = {
    "Initial JEFS Sold": ["Net New Deal", "Addendum", "Renewal"],
    "Expansion for Existing JEFS": ["Expansion Deal", "Renewal Deal"]
}

deal_type = st.selectbox(
    "Select Deal Type",
    deal_type_options[subcategory]
)

# Step 4: Show Relevant Inputs
st.write("### Enter Deal Details:")
total_amount = st.number_input("Total Amount ($)", min_value=0.0, step=0.01)
total_term = st.number_input("Total Term (months)", min_value=1, step=1)

# Additional fields for specific deal types
addendum_amount = remaining_term = net_new_amount = 0

if deal_type == "Addendum":
    addendum_amount = st.number_input("Addendum Amount ($)", min_value=0.0, step=0.01)
    remaining_term = st.number_input("Remaining Term (months)", min_value=1, step=1)
    net_new_amount = st.number_input("Net New Amount ($)", min_value=0.0, step=0.01)
elif deal_type in ["Expansion Deal"]:
    remaining_term = st.number_input("Remaining Term (months)", min_value=1, step=1)


commission_rate = 0.15 
monthly_commission = 0

if st.button("Calculate Commission"):
    if deal_type == "Net New Deal":
        monthly_commission = (total_amount / total_term) * commission_rate
    elif deal_type == "Addendum":
        monthly_commission = ((addendum_amount / remaining_term) + (net_new_amount / total_term)) * commission_rate
    elif deal_type == "Renewal":
        monthly_commission = (total_amount / total_term) * commission_rate
    elif deal_type == "Expansion Deal":
        monthly_commission = (total_amount / remaining_term) * commission_rate
    elif deal_type == "Renewal Deal":
        monthly_commission = (total_amount / total_term) * commission_rate

    annual_commission = monthly_commission * 12

    # Display the results
    st.subheader("Commission Results:")
    st.write(f"**Monthly Commission:** ${monthly_commission:.2f}")
    st.write(f"**Annual Commission:** ${annual_commission:.2f}")
