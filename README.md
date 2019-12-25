# これなに
異常終了したECSタスクをSlackに通知する

# でぽろい

```
s3bucket=aaa
s3prefix=bbb
stackname=ccc

sam package \
--template-file template.yaml \
--output-template sam-output.yaml \
--s3-bucket ${s3bucket} \
--s3-prefix ${s3prefix}

sam deploy \
--template-file sam-output.yaml \
--stack-name ${stackname} \
--capabilities CAPABILITY_NAMED_IAM
```
