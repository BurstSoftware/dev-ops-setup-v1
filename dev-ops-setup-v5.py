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

def lambda_guide_page():
    st.title("AWS Lambda Guide")
    
    # Introduction
    st.markdown("""
    This guide will help you create and manage serverless functions using AWS Lambda.
    """)
    
    # Section 1: Lambda Basics
    st.header("1. Understanding AWS Lambda")
    with st.expander("View Lambda Basics", expanded=True):
        st.markdown("""
        - Serverless compute service
        - Runs code in response to events
        - Automatic scaling
        - Pay-per-use pricing
        
        Common use cases:
        * Processing file uploads
        * Real-time data processing
        * API backend services
        * Scheduled tasks
        """)
    
    # Section 2: Creating a Lambda Function
    st.header("2. Creating Your First Lambda Function")
    with st.expander("View Creation Steps", expanded=True):
        st.markdown("""
        1. Log in to AWS Console
        2. Search for "Lambda" in the services menu
        3. Click "Create function"
        4. Choose options:
           * Author from scratch
           * Function name: "MyFirstLambda"
           * Runtime: Python 3.9
           * Architecture: x86_64
        5. Click "Create function"
        """)
        
        st.subheader("Sample Lambda Code")
        lambda_code = '''import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }'''
        st.code(lambda_code, language="python")
    
    # Section 3: Configuration
    st.header("3. Configuring Lambda")
    with st.expander("View Configuration Details", expanded=True):
        st.markdown("""
        Basic Settings:
        * Memory: 128 MB (default)
        * Timeout: 3 seconds (default)
        * Execution role: Create new role with basic Lambda permissions
        
        Triggers:
        1. Click "Add trigger"
        2. Select from:
           * API Gateway
           * CloudWatch Events
           * S3
           * SNS
        """)
        
        st.info("💡 Tip: Start with minimal permissions and add as needed using IAM policies.")

def bigquery_setup_page():
    st.title("Google Cloud BigQuery Setup")
    
    # Introduction
    st.markdown("""
    Follow these steps to set up Google Cloud BigQuery for CloudMart
    """)
    
    # Step 1: Create Project
    st.header("1. Create a Google Cloud Project")
    with st.expander("View Project Creation Steps", expanded=True):
        st.markdown("""
        1. Go to the Google Cloud Console: [https://console.cloud.google.com/](https://console.cloud.google.com/)
        2. Click on the project dropdown and select "New Project"
        3. Name the project "CloudMart" and create it
        """)
    
    # Step 2: Enable BigQuery API
    st.header("2. Enable BigQuery API")
    with st.expander("View API Enablement Steps", expanded=True):
        st.markdown("""
        1. In the Google Cloud Console, go to "APIs & Services" > "Dashboard"
        2. Click "+ ENABLE APIS AND SERVICES"
        3. Search for "BigQuery API" and enable it
        """)
    
    # Step 3: Create Dataset
    st.header("3. Create a BigQuery Dataset")
    with st.expander("View Dataset Creation Steps", expanded=True):
        st.markdown("""
        1. In the Google Cloud Console, go to "BigQuery"
        2. In the Explorer pane, click on your project name
        3. Click "CREATE DATASET"
        4. Set the Dataset ID to "cloudmart"
        5. Choose your data location and click "CREATE DATASET"
        """)
    
    # Step 4: Create Table
    st.header("4. Create a BigQuery Table")
    with st.expander("View Table Creation Steps", expanded=True):
        st.markdown("""
        1. In the dataset you just created, click "CREATE TABLE"
        2. Set the Table name to "cloudmart-orders"
        3. Define the schema according to your order structure:
        """)
        
        schema_code = '''- id: STRING
- items: JSON
- userEmail: STRING
- total: FLOAT
- status: STRING
- createdAt: TIMESTAMP'''
        st.code(schema_code, language="plaintext")
        
        st.markdown("""
        4. Click "CREATE TABLE"
        """)

def main():
    st.set_page_config(
        page_title="Cloud Development Guide",
        page_icon="🚀",
        layout="wide"
    )
    
    # Updated Page Navigation with new page
    page = st.sidebar.radio(
        "Navigation", 
        ["Terraform Guide", 
         "AWS & Docker Guide", 
         "GitHub & CodePipeline Guide",
         "AWS Lambda Guide",
         "Google BigQuery Setup"]
    )
    
    # Updated page routing
    if page == "Terraform Guide":
        main_page()
    elif page == "AWS & Docker Guide":
        aws_docker_page()
    elif page == "GitHub & CodePipeline Guide":
        github_codepipeline_page()
    elif page == "AWS Lambda Guide":
        lambda_guide_page()
    else:
        bigquery_setup_page()
    
    # Common Resources Sidebar (updated with BigQuery docs)
    st.sidebar.header("Resources")
    st.sidebar.markdown("""
    - [AWS Documentation](https://docs.aws.amazon.com)
    - [Docker Documentation](https://docs.docker.com)
    - [Terraform Documentation](https://www.terraform.io/docs)
    - [GitHub Documentation](https://docs.github.com)
    - [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
    - [Google BigQuery Documentation](https://cloud.google.com/bigquery/docs)
    """)
    
    # Updated Progress Tracking with new page checkpoints
    st.sidebar.header("Progress Tracking")
    if page == "Terraform Guide":
        st.sidebar.checkbox("✅ Complete Terraform Setup")
        st.sidebar.checkbox("✅ Launch EC2 Instance")
    elif page == "AWS & Docker Guide":
        st.sidebar.checkbox("✅ Create DynamoDB Table")
        st.sidebar.checkbox("✅ Setup Docker Environment")
    elif page == "GitHub & CodePipeline Guide":
        st.sidebar.checkbox("✅ Create GitHub Account")
        st.sidebar.checkbox("✅ Setup CodePipeline")
    elif page == "AWS Lambda Guide":
        st.sidebar.checkbox("✅ Create Lambda Function")
        st.sidebar.checkbox("✅ Configure Lambda Trigger")
    else:
        st.sidebar.checkbox("✅ Create BigQuery Dataset")
        st.sidebar.checkbox("✅ Create BigQuery Table")

if __name__ == "__main__":
    main()
