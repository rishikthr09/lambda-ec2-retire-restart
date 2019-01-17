# lambda-ec2-retire-restart
Simple lambda function to restart ec2 instances scheduled for retirement based on cloudwatch event.
Can be used for non-persistent replicated ec2 instances (k8s worker)

- add policy and attach to lambda role
- use role to deploy lambda function
- use event trigger yml for lambda

<sub><sup>
Isn't this very specific for this use-case? Yes it is. But AWS documentation sucks for this relatively-critical scenario in production -_-
</sup></sub>
