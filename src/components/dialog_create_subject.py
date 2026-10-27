import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")

def create_subject_dialog(teacher_id):

    st.write("Enter the details of new subject")
    
    sub_id = st.text_input("Subject Code", placeholder="CS101")
    sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="A")
   
    if st.button("Create Subject Now", type='primary', width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast("Subject Created Succesfully!")
                st.rerun()

            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:    
            st.warning("Please fill all the fields")



# import streamlit as st
# from src.database.db import create_subject


# @st.dialog("Create New Subject")
# def create_subject_dialog(teacher_id):
#     st.write("Enter the details of new subject")
#     sub_id = st.text_input("Subject Code", placeholder="CS101")
#     sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science")
#     sub_section = st.text_input("Section", placeholder="A")

#     if st.button("Create Subject Now", type='primary', width='stretch'):
#         if sub_id and sub_name and sub_section:
#             try:
#                 create_subject(sub_id, sub_name, sub_section, teacher_id)
#                 st.toast("Subject Created Successfully!")
#                 st.rerun()
#             except Exception as e:
#                 st.error(f"Error: {str(e)}")
#         else:
#             st.warning("Please fill all the fields")


# @st.dialog("Share Subject")
# def share_subject_dialog(name, code):
#     st.write(f"Share the subject code for **{name}** with your students.")
#     st.code(code)

#     if st.button("Close", width='stretch'):
#         st.rerun()


# def subject_card(name, code, section, stats, footer_callback=None):
#     with st.container(border=True):
#         st.subheader(name)
#         st.write(f"Subject Code: {code}")
#         st.write(f"Section: {section}")

#         col1, col2 = st.columns(2)

#         with col1:
#             st.metric(stats[0][1], stats[0][2])

#         with col2:
#             st.metric(stats[1][1], stats[1][2])

#         if footer_callback:
#             footer_callback()

