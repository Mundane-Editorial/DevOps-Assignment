Step 1. create Backup vault
<code>
Aws console > aws backup > backup vaults > create new vault > select 'AWS KMS encryption key' > click 'Create Backup Vault'
</code>
<br>
Step 2. create backup plan
go to <code>AWS backup > backup plans > create backup plan </code>
<code>Build new plan > provide Name > define backup rules by selecting your vault > define your backup parameters > click 'create plan'</code>
<br>
Step 3. Assign resources to backup plan
go to<code>Aws Backup > Backup plan > click 'assign resources' > provide Resource Assignment Name > select/create IAMRole > assign your resources > Assign Resources</code>
<br>
Step 4. Enable continuous backup
<code>AWS Backup > Backup valut > 'mybackupvault' > enable 'continuous backups' > define retention period > apply</code>

