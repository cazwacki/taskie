# Caller

A Lambda function that reads out a user's taskie message back to them via phone call.

### Environment Variables

- `INSTANCE_ID`: The ID of the Amazon Connect instance. An instance ARN has the following format: `arn:aws:connect:<region>:<account>:instance/<instance id>`.
- `CONTACT_FLOW_ID`: The ID of the inbound contact flow configured in the Amazon Connect instance provided by `INSTANCE_ID`. A contact flow ARN has the following format: `arn:aws:connect:<region>:<account>:instance/<instance id>/contact-flow/<contact flow id>`
- `SOURCE_PHONE_NUMBER`: A source phone number claimed by the Amazon Connect Instance provided in `INSTANCE_ID`.

### Event Inputs

- `taskie_id`: The ID associated with the taskie
- `message`: The string to read back to the user
- `destination_phone_number`: The phone number to which the outbound call is made