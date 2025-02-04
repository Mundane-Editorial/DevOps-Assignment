<h2>AWS EC2 (Elastic Compute Cloud)</h2>
Instance Type: Ubuntu-based EC2 instance.
Instance Role: Hosted the Docker container running your Node.js application.
Public IP: Used to access the website externally.

<hr>

<h2> AWS Security Groups</h2>
Inbound Rule: Allowed TCP traffic on port 3000 from external sources (0.0.0.0/0 for public access).
<br>
Command used (inside AWS console):
Open EC2 Dashboard → Security Groups → Modify Inbound Rules.
Allowed port 3000 for public access.

<hr>

<h2>Docker</h2>
to pull image from docker hub and run it, ensuring a consistent environment across deployments.