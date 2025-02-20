import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(
        page_title="Claude Terraform Guide",
        page_icon="🤖",
        layout="wide"
    )

    st.title("Streamlined Guide: Using Claude as AI Assistant to Terraform")
    
    # Introduction
    st.markdown("""
    This guide will walk you through the process of using Claude AI to generate Terraform code
    and set up your AWS infrastructure.
    """)

    # Step 1
    st.header("Step 1: Use Claude to Generate Terraform Code")
    
    with st.expander("View Step 1 Details", expanded=True):
        st.markdown("""
        1. Create a FREE account with Claude: [claude.ai](https://claude.ai)
        2. Start a conversation with Claude
        3. Ask Claude to create Terraform code for an S3 bucket using this prompt:
        """)
        
        prompt_box = st.code(
            '"Please provide Terraform code to create an S3 bucket in AWS with a unique name."',
            language="markdown"
        )
        
        st.markdown("### Sample Generated Code")
        
        terraform_code = '''provider "aws" {
  region = "us-west-2"  # Replace with your desired region
}

resource "random_id" "bucket_suffix" {
  byte_length = 8
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-unique-bucket-name-${random_id.bucket_suffix.hex}"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket_acl" "my_bucket_acl" {
  bucket = aws_s3_bucket.my_bucket.id
  acl    = "private"
}'''
        
        st.code(terraform_code, language="hcl")

    # Step 2
    st.header("Step 2: Launch EC2 Instance")
    
    with st.expander("View Step 2 Details", expanded=True):
        st.markdown("""
        1. Create a FREE AWS account: [aws.amazon.com/free](https://aws.amazon.com/free/)
        2. Go to the EC2 dashboard in the AWS Management Console
        3. Click "Launch Instance"
        4. Choose an Amazon Linux 2 AMI
        5. Select a t2.micro instance type
        6. Configure instance details:
            * Network: Default VPC
            * Subnet: Any available
            * Auto-assign Public IP: Enable
            * IAM role: Select "EC2Admin"
        7. Keep default storage settings
        8. Add a tag: Key="Name", Value="workstation"
        9. Create a security group allowing SSH access from EC2 Connect IP
        10. Review and launch, selecting or creating a key pair
        """)

    # Progress Tracker
    st.header("Progress Tracker")
    col1, col2 = st.columns(2)
    
    with col1:
        st.checkbox("Created Claude Account")
        st.checkbox("Generated Terraform Code")
        
    with col2:
        st.checkbox("Created AWS Account")
        st.checkbox("Launched EC2 Instance")

    # Success Message
    if st.button("Mark as Complete"):
        st.success("""
        🎉 Congratulations! You've successfully used Claude to generate Terraform code 
        and set up an EC2 workstation! This completes Day 1 of the MultiCloud DevOps & AI Challenge.
        """)

    # Additional Resources
    st.sidebar.header("Resources")
    st.sidebar.markdown("""
    - [Claude AI Documentation](https://docs.anthropic.com)
    - [AWS Documentation](https://docs.aws.amazon.com)
    - [Terraform Documentation](https://www.terraform.io/docs)
    """)

if __name__ == "__main__":
    main()
