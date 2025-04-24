import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="电池寿命预测系统", page_icon="🔋")

st.title("电池寿命预测系统")
st.write("基于机器学习的电池SOH和RUL预测")

st.sidebar.title("导航")
page = st.sidebar.selectbox("选择功能", ["首页", "数据上传", "模型训练", "预测结果"])

if page == "首页":
    st.header("欢迎使用电池寿命预测系统")
    st.write("本系统可以帮助您预测电池的健康状态(SOH)和剩余使用寿命(RUL)。")
    st.write("请使用左侧导航栏选择功能。")
    
    st.image("https://img.icons8.com/color/96/000000/battery-level.png", width=200) 
    
    st.subheader("系统功能")
    st.write("- 数据上传与预处理")
    st.write("- 探索性数据分析")
    st.write("- 特征提取")
    st.write("- 模型训练")
    st.write("- SOH和RUL预测")

elif page == "数据上传":
    st.header("数据上传")
    st.write("上传电池数据文件（支持CSV和Excel格式）")
    
    uploaded_file = st.file_uploader("选择数据文件", type=["csv", "xlsx", "xls"])
    
    if uploaded_file is not None:
        st.success(f"文件 {uploaded_file.name} 上传成功！")
        st.write("在完整版本中，系统将自动处理您的数据。")

elif page == "模型训练":
    st.header("模型训练")
    
    model_type = st.selectbox("选择模型类型", ["随机森林", "SVR", "XGBoost", "LSTM"])
    
    if st.button("训练模型"):
        with st.spinner("正在训练模型..."):
            # 模拟训练过程
            import time
            time.sleep(2)
            st.success("模型训练完成！")
            
            # 显示模拟的评估指标
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("R²", "0.9542")
            col2.metric("MAE", "0.0124")
            col3.metric("MSE", "0.0003")
            col4.metric("RMSE", "0.0173")

elif page == "预测结果":
    st.header("预测结果")
    
    # 模拟数据
    cycles = np.arange(0, 500)
    soh = 100 * np.exp(-0.001 * cycles)
    
    # EOL阈值
    eol_threshold = st.slider("EOL阈值 (SOH百分比)", 50, 90, 80) / 100.0
    
    # 找到EOL点
    eol_cycle = next((i for i, s in enumerate(soh) if s < eol_threshold * 100), len(cycles) - 1)
    
    # 绘制SOH曲线
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(cycles, soh, 'b-', label='预测SOH')
    ax.axhline(y=eol_threshold * 100, color='r', linestyle='--', label=f'EOL阈值 ({eol_threshold*100:.0f}%)')
    ax.plot(eol_cycle, eol_threshold * 100, 'ro', markersize=10)
    ax.set_title("SOH预测")
    ax.set_xlabel("循环次数")
    ax.set_ylabel("SOH (%)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    
    st.info(f"预测RUL: {eol_cycle} 循环")

# 页脚
st.markdown("---")
st.markdown("### 电池寿命预测系统 | 基于机器学习的SOH和RUL预测")
st.markdown("© 2025 电池健康管理团队")
