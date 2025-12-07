import streamlit as st
from database.db import load_opportunities, save_opportunities

st.set_page_config(page_title="Artist Dashboard", layout="wide")

st.title("🎨 Artist Promotion Assistant – Dashboard")
st.write("Approve or reject AI-detected opportunities.")

opps = load_opportunities()

if not opps:
    st.info("No opportunities yet. Keep the monitor running.")
else:
    for i, opp in enumerate(opps):
        with st.container():
            st.subheader(f"@{opp['username']} on {opp['platform']}")
            st.write(f"**Message:** {opp['text']}")
            st.write(f"**Score:** {opp['score']}")
            st.write("**AI Suggested Reply:**")
            st.success(opp["ai_reply"])

            col1, col2 = st.columns(2)

            if col1.button("Approve", key=f"approve_{i}"):
                opp["status"] = "approved"
                save_opportunities(opps)
                st.success("Approved!")
                st.experimental_rerun()

            if col2.button("Reject", key=f"reject_{i}"):
                opp["status"] = "rejected"
                save_opportunities(opps)
                st.error("Rejected!")
                st.experimental_rerun()

st.write("---")
st.write("Run live monitoring:")
st.code("python -m monitor.stream")
