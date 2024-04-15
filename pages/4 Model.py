import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title(':card_index: Mô hình dự đoán khách hàng rời bỏ')

# Load mô hình
model = joblib.load('logistic_regression_model.pkl')

##
st.write('Vui lòng nhập đầu vào:')
with st.expander('Nhập thông tin ở đây:'):
    inputs = {}
    st.subheader('**Thông tin về khách hàng**')

    st.write('**1. Giới tính của khách hàng**')
    gender = st.selectbox('*Vui lòng chọn:*', ['Male', 'Female'])

    st.write('**2. Tuổi của khách hàng**')
    age = st.slider('*Vui lòng kéo chọn:*', min_value=18, max_value=100)

    st.write('**3. Tình trạng hôn nhân của khách hàng** *(:heavy_check_mark: nếu khách hàng Đã kết hôn)*')
    inputs['Married'] = st.checkbox('Đã kết hôn')

    st.write('**4. Khách hàng có ở chung với người thân** *(:heavy_check_mark: nếu Có)*')
    dependents_checkbox = st.checkbox('Sống chung với người thân')
    st.write('**5. Số người thân ở chung**  *(Nếu không có mục 4 vui lòng bỏ qua)* ')
    if dependents_checkbox:
        num_dependents = st.slider('*Vui lòng kéo chọn số người:*', min_value=1, max_value=15)
    else:
        num_dependents = 0
        st.empty()

    st.write('**6. Khách hàng có giới thiệu dịch vụ với người thân** *(:heavy_check_mark: nếu Có)*')
    referred_checkbox = st.checkbox('Giới thiệu cho người thân')
    st.write('**7. Số người được giới thiệu**  *(Nếu không có mục 6 vui lòng bỏ qua)*')
    if referred_checkbox:
        num_referrals = st.slider('*Vui lòng kéo chọn số người:*', min_value=1, max_value=20)
    else:
        num_referrals = 0
        st.empty()




    ##
    st.subheader('**Thông tin về dịch vụ**')

    st.write('**1. Số tháng gắn bó**')
    tenure_months = st.slider('*Vui lòng kéo chọn:*', min_value=1, max_value=120)

    st.write('**2. Điểm hài lòng**')
    satisfaction_score = st.slider('*Vui lòng kéo chọn*', min_value=1, max_value=5)

    st.write('**3. Điểm rời bỏ**')
    churn_score = st.slider('*Vui lòng kéo chọn*', min_value=0, max_value=150, step=1)

    st.write('**4. Điểm vòng đời khách hàng**')
    cltv = st.slider('*Vui lòng kéo chọn*', min_value=2000, max_value=10000, step=1)


    st.write('**5. Loại yêu cầu**')
    offer = st.selectbox('*Vui lòng chọn*', ['Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E', 'No Offer'])

    st.write('**6. Loại Internet**')
    internet_type = st.selectbox('*Vui lòng chọn*', ['DSL', 'Fiber Optic', 'Cable', 'No Internet Type'])

    st.write('**7. Loại hợp đồng**')
    contract = st.selectbox('*Vui lòng chọn*', ['Month-to-Month', 'One Year', 'Two Year'])

    st.write('**8. Loại thanh toán**')
    payment_method = st.selectbox('*Vui lòng chọn*', ['Bank Withdrawal', 'Credit Card', 'Mailed Check'])


    st.write('**7. Các loại dịch vụ mà khách hàng sử dụng** *(Chỉ :heavy_check_mark: vào những Dịch vụ có sử dụng )*')
    # Tạo các checkbox và lưu giá trị vào một dictionary
    inputs['Phone Service'] = st.checkbox('Phone Service')
    inputs['Multiple Lines'] = st.checkbox('Multiple Lines')
    inputs['Internet Service'] = st.checkbox('Internet Service')
    inputs['Online Security'] = st.checkbox('Online Security')
    inputs['Online Backup'] = st.checkbox('Online Backup')
    inputs['Device Protection Plan'] = st.checkbox('Device Protection Plan')
    inputs['Premium Tech Support'] = st.checkbox('Premium Tech Support')
    inputs['Streaming TV'] = st.checkbox('Streaming TV')
    inputs['Streaming Movies'] = st.checkbox('Streaming Movies')
    inputs['Streaming Music'] = st.checkbox('Streaming Music')
    inputs['Unlimited Data'] = st.checkbox('Unlimited Data')
    inputs['Paperless Billing'] = st.checkbox('Paperless Billing')


    st.write('**8. Các loại phí**')
    st.write('*Vui lòng điền vào những loại phí dịch vụ mà khách hàng sử dụng (Nếu không có thì bỏ qua)*')
    avg_long_distance_charges = st.number_input('Avg Monthly Long Distance Charges', min_value=0.0, max_value=80.0, step=0.01)
    avg_gb_download = st.number_input('Avg Monthly GB Download', min_value=0, max_value=150, step=1)
    monthly_charge = st.number_input('Monthly Charge', min_value=0.0, max_value=200.0, step=0.01)
    total_charges = st.number_input('Total Charges', min_value=0.0, max_value=10000.0, step=0.01)
    total_refunds = st.number_input('Total Refunds', min_value=0.0, max_value=80.0, step=0.01)
    total_extra_data_charges = st.number_input('Total Extra Data Charges', min_value=0, max_value=200, step=1)
    total_long_distance_charges = st.number_input('Total Long Distance Charges', min_value=0.0, max_value=4000.0, step=0.01)
    total_revenue = st.number_input('Total Revenue', min_value=0.0, max_value=15000.0, step=0.01)



    inputs = {
        'Gender': gender,
        'Age': age,
        'Married': 1 if inputs.get('Married') else 0,
        'Dependents': 1 if dependents_checkbox else 0,
        'Num Dependents': num_dependents,
        'Referred a Friend': 1 if referred_checkbox else 0,
        'Num Referrals': num_referrals,
        'Tenure in Months': tenure_months,
        'Offer': offer,
        'Phone Service': 1 if inputs.get('Phone Service') else 0,
        'Avg Monthly Long Distance Charges': avg_long_distance_charges,
        'Multiple Lines': 1 if inputs.get('Multiple Lines') else 0,
        'Internet Service': 1 if inputs.get('Internet Service') else 0,
        'Internet Type': internet_type,
        'Avg Monthly GB Download': avg_gb_download,
        'Online Security': 1 if inputs.get('Online Security') else 0,
        'Online Backup': 1 if inputs.get('Online Backup') else 0,
        'Device Protection Plan': 1 if inputs.get('Device Protection Plan') else 0,
        'Premium Tech Support': 1 if inputs.get('Premium Tech Support') else 0,
        'Streaming TV': 1 if inputs.get('Streaming TV') else 0,
        'Streaming Movies': 1 if inputs.get('Streaming Movies') else 0,
        'Streaming Music': 1 if inputs.get('Streaming Music') else 0,
        'Unlimited Data': 1 if inputs.get('Unlimited Data') else 0,
        'Contract': contract,
        'Paperless Billing': 1 if inputs.get('Paperless Billing') else 0,
        'Payment Method': payment_method,
        'Monthly Charge': monthly_charge,
        'Total Charges': total_charges,
        'Total Refunds': total_refunds,
        'Total Extra Data Charges': total_extra_data_charges,
        'Total Long Distance Charges': total_long_distance_charges,
        'Total Revenue': total_revenue,
        'Satisfaction Score': satisfaction_score,
        'Churn Score': churn_score,
        'CLTV': cltv
    }


    # Chuyển các cột khác sang biến định lượng, không có giá trị mặc định
    inputs['Gender'] = 0 if gender == 'Male' else 1
    inputs['Offer'] = {'Offer A': 1, 'Offer B': 2, 'Offer C': 3, 'Offer D': 4, 'Offer E': 5, 'No Offer':6}.get(inputs['Offer'])
    inputs['Internet Type'] = {'DSL': 1, 'Fiber Optic': 2, 'Cable': 3, 'No Internet Type': 4}.get(inputs['Internet Type'])
    inputs['Contract'] = {'Month-to-Month': 1, 'One Year': 2, 'Two Year': 3}.get(inputs['Contract'])
    inputs['Payment Method'] = {'Bank Withdrawal': 1, 'Credit Card': 2, 'Mailed Check': 3}.get(inputs['Payment Method'])

# Hiển thị dictionary inputs
#st.write(inputs)
#print(inputs)
##

def predict():
    # Chuyển đổi dữ liệu đầu vào thành DataFrame để chuẩn hóa
    input_df = pd.DataFrame([inputs])

    ##Model
    prediction = model.predict(input_df)
    

    ##Ouput
    if prediction == 1:
        st.error('Khách hàng rời bỏ :sob:')
    else:
        st.success('Khách hàng ở lại :hugging_face:')

st.button('Predict', on_click=predict)





