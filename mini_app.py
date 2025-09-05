import streamlit as st
st.title("Environment Check")
import sys, platform
st.write("Python:", sys.version)
st.write("Platform:", platform.platform())

ok, errs = {}, {}
for name in ["yfinance","pandas","numpy","requests"]:
    try:
        mod = __import__(name)
        ok[name] = getattr(mod, "__version__", "OK")
    except Exception as e:
        errs[name] = str(e)

st.subheader("Imports")
st.write("OK:", ok)
st.write("Errors:", errs)