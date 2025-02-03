import streamlit as st


st.title("Commission Calculator")


deal_type = st.selectbox(
    "Select Deal Type",
    ["Net New Deal", "Addendum", "Renewal", "Expansion Deal", "Renewal Deal"]
)


total_amount = st.number_input("Total Amount ($)", min_value=0.0, step=0.01)
total_term = st.number_input("Total Term (months)", min_value=1, step=1)

addendum_amount = remaining_term = net_new_amount = 0

if deal_type == "Addendum":
    addendum_amount = st.number_input("Addendum Amount ($)", min_value=0.0, step=0.01)
    remaining_term = st.number_input("Remaining Term (months)", min_value=1, step=1)
    net_new_amount = st.number_input("Net New Amount ($)", min_value=0.0, step=0.01)
elif deal_type == "Expansion Deal":
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

    
    st.subheader("Commission Results:")
    st.write(f"**Monthly Commission:** ${monthly_commission:.2f}")
    st.write(f"**Annual Commission:** ${annual_commission:.2f}")
