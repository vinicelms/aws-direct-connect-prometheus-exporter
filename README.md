# AWS Direct Connect status exporter

Export AWS Direct Connect status.

It was developed to list all Direct Connects in a region and later lists the virtual interfaces associated with Direct Connect, along with the status of each item.

## How to use
Because the project is allowed to list AWS connections, it has some prerequisites for it to operate, such as:
- AWS user
  - AWS Access Key
  - AWS Secret Key
- Region in which Direct Connect is associated
- Create restrictive user policy (for security reasons)

## Environment variables
- AWS_ACCESS_KEY
- AWS_SECRET_KEY
- AWS_REGION

To do this, run (Linux):
```
export AWS_ACCESS_KEY=ABCDEFGHIJKLMNOPQRST
export AWS_SECRET_KEY=BTyfO'i3oHkVbTRU1@>HkLg71HgMD\;$DgeVa?K_
export AWS_REGION=us-east-1
```

## Minimal AWS Policy

If you want to list only a few Direct Connects, define the resources via the AWS console in policy management or else define the ARN for each feature directly in JSON below.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "directconnect:DescribeConnections",
                "directconnect:DescribeVirtualInterfaces"
            ],
            "Resource": "*"
        }
    ]
}
```