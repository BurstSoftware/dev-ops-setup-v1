import streamlit as st
import streamlit.components.v1 as components

def main_page():
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

def aws_docker_page():
    st.title("AWS DynamoDB & Docker Guide")
    
    # AWS Access Section
    st.header("1. Accessing AWS")
    st.markdown("""
    * Access the AWS console at [aws.amazon.com](https://aws.amazon.com)
    * Log in with your credentials
    * Select the desired region in the upper right corner
    """)
    
    # DynamoDB Section
    st.header("2. Creating a Table in DynamoDB")
    with st.expander("View DynamoDB Steps", expanded=True):
        st.markdown("""
        1. In the AWS console search bar, type "DynamoDB"
        2. Click on "Create table"
        3. Define the table name
        4. Configure the partition key
        5. Choose capacity settings (on-demand or provisioned)
        6. Review and click on "Create table"
        """)
    
    # Docker Hub Section
    st.header("3. Exploring Docker Hub")
    with st.expander("View Docker Hub Steps", expanded=True):
        st.markdown("""
        1. Visit [hub.docker.com](https://hub.docker.com)
        2. Create an account or log in (optional for searching images)
        3. Use the search bar to find official images
        4. Explore available tags for each image
        5. Check documentation and usage examples
        """)
        
        # Tip callout using custom styling
        st.info("💡 Tip: Always prefer official or verified images on Docker Hub for better security and reliability.")
    
    # Docker Commands Section
    st.header("Basic Docker Commands")
    docker_commands = '''# Search for an image
docker pull image-name

# List local images
docker images

# Run a container
docker run image-name

# List running containers
docker ps'''
    
    st.code(docker_commands, language="bash")
    
    st.markdown("""
    Remember to always check the official AWS and Docker documentation for more detailed and up-to-date information.
    """)

def main():
    st.set_page_config(
        page_title="Cloud Development Guide",
        page_icon="🚀",
        layout="wide"
    )
    
    # Page Navigation
    page = st.sidebar.radio("Navigation", ["Terraform Guide", "AWS & Docker Guide"])
    
    if page == "Terraform Guide":
        main_page()
    else:
        aws_docker_page()
    
    # Common Resources Sidebar
    st.sidebar.header("Resources")
    st.sidebar.markdown("""
    - [AWS Documentation](https://docs.aws.amazon.com)
    - [Docker Documentation](https://docs.docker.com)
    - [Terraform Documentation](https://www.terraform.io/docs)
    """)

if __name__ == "__main__":
    main()
