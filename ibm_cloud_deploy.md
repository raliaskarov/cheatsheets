# Commands on IBM Cloud Deploy

Deploy command
```
ibmcloud ce application create --name prodlist --image us.icr.io/${SN_ICR_NAMESPACE}/prodlist --registry-secret icr-secret --port 5000 --build-context-dir products_list --build-source https://github.com/ibm-developer-skills-network/dealer_evaluation_backend.git
```

In this code:
* **build-source** - https://github.com/ibm-developer-skills-network/dealer_evaluation_backend.git
* **build-context-dir** - dealer_details
* **port** - 8080
* **name** - dealerdetails
* **image** - us.icr.io/${SN_ICR_NAMESPACE}/dealerdetails
