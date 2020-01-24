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