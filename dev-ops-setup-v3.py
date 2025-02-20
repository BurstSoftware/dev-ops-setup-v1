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

def github_codepipeline_page():
    st.title("GitHub & AWS CodePipeline Guide")
    
    # GitHub Account Creation
    st.header("Create a GitHub Account")
    with st.expander("GitHub Account Setup Steps", expanded=True):
        st.markdown("""
        1. Go to [github.com](https://github.com)
        2. Click "Sign up" in the top right corner
        3. Enter your email
        4. Create a strong password
        5. Choose a unique username
        6. Confirm your email through the verification code
        7. Complete the personalization questions (optional)
        """)
        
        st.subheader("Creating a New Repository")
        st.markdown("""
        * Click the "+" button in the top right corner
        * Select "New repository"
        * Give your repository a name
        * Choose whether it will be public or private
        * Initialize with a README if desired
        * Click "Create repository"
        """)
    
    # AWS CodePipeline Section
    st.header("Exploring AWS CodePipeline")
    with st.expander("CodePipeline Navigation Guide", expanded=True):
        st.markdown("""
        1. Log in to the AWS Console at [console.aws.amazon.com](https://console.aws.amazon.com)
        2. In the top search bar, type "CodePipeline" and select the service
        """)
        
        st.subheader("CodePipeline Homepage Overview")
        st.markdown("""
        3. On the CodePipeline homepage:
           * Observe the main panel showing your existing pipelines
           * Note the "Create pipeline" button in the top right corner
           * Explore the left sidebar to see other available options
        """)
        
        st.subheader("Pipeline Creation Process")
        st.markdown("""
        4. Click "Create pipeline" to explore the creation wizard:
           * Examine the source code options (GitHub, CodeCommit, S3)
           * See the different build providers available
           * Explore the deployment options
        """)
        
        st.subheader("Managing Existing Pipelines")
        st.markdown("""
        5. In the existing pipelines section:
           * Observe the visual structure of pipelines
           * See the different states (Success, In Progress, Failed)
           * Explore the execution history options
        """)
        
        st.subheader("Configuration Settings")
        st.markdown("""
        6. Explore the settings:
           * Examine the notification settings
           * View the logging options
           * Explore the permission policies
        """)

def main():
    st.set_page_config(
        page_title="Cloud Development Guide",
        page_icon="🚀",
        layout="wide"
    )
    
    # Page Navigation
    page = st.sidebar.radio(
        "Navigation", 
        ["Terraform Guide", "AWS & Docker Guide", "GitHub & CodePipeline Guide"]
    )
    
    if page == "Terraform Guide":
        main_page()
    elif page == "AWS & Docker Guide":
        aws_docker_page()
    else:
        github_codepipeline_page()
    
    # Common Resources Sidebar
    st.sidebar.header("Resources")
    st.sidebar.markdown("""
    - [AWS Documentation](https://docs.aws.amazon.com)
    - [Docker Documentation](https://docs.docker.com)
    - [Terraform Documentation](https://www.terraform.io/docs)
    - [GitHub Documentation](https://docs.github.com)
    """)
    
    # Progress Tracking
    st.sidebar.header("Progress Tracking")
    if page == "Terraform Guide":
        st.sidebar.checkbox("✅ Complete Terraform Setup")
        st.sidebar.checkbox("✅ Launch EC2 Instance")
    elif page == "AWS & Docker Guide":
        st.sidebar.checkbox("✅ Create DynamoDB Table")
        st.sidebar.checkbox("✅ Setup Docker Environment")
    else:
        st.sidebar.checkbox("✅ Create GitHub Account")
        st.sidebar.checkbox("✅ Setup CodePipeline")

if __name__ == "__main__":
    main()
