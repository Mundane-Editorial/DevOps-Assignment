<h3>self Declaration : I didn't tried to deploy this project because of deadline adn my model is not working as expected, though, i'm leaving the steps to deploy.</h3>

Step 1 : build and push your docker image to docker hub (run on localhost first for testing) 
Step 2 : Deploy the model on kubernetes using deployment.yml and service.yml file using
<code>
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
</code>
Step 3 : Verify 
<code>kubectl get pods</code> : to check whether pods are running or not
<code>kubectl get svc</code> : for service details
<hr>
* get the External ip using <code> minikube service "service-name" --url</code> :: for me, service-name = facial-emotion-model-service
<br>
<h3>Verfy deployment</h3>
using <code>curl http://External-ip:5000/predict
</code>
