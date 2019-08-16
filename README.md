# aws-iam-report

Creating an AWS IAM Report for auditing purpose.

#### Open list_user.py and add the parameters you want it in the report

### The parameters list are as below:

- user
- arn
- user_creation_time
- password_enabled
- password_last_used
- password_last_changed
- password_next_rotation
- mfa_active
- access_key_1_active
- access_key_1_last_rotated
- access_key_1_last_used_date
- access_key_1_last_used_region
- access_key_1_last_used_service
- access_key_2_active
- access_key_2_last_rotated
- access_key_2_last_used_date
- access_key_2_last_used_region
- access_key_2_last_used_service
- cert_1_active
- cert_1_last_rotated
- cert_2_active
- cert_2_last_rotated

```

aws iam get-credential-report | ./list_user.py > output.txt

```

Incase if you want to print a particular paramter, you can use ```awk``` to fetch the value

```

aws iam get-credential-report | ./list_user.py > output.txt | awk {'print $2'}

```
