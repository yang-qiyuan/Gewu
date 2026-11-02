## P-tuning
```
It used a prompt encoder to encode the prompt to continuous hidden state and then finetune the model.
```
![ptuning](../resources/img/llms/ptuning.png)

### Limitations
- performs bad on label sequence task
- hard to scale up
## P-tuning v2
```
It adds trainable prompt vectors to every layers and throw the verbalizer away since the verbalizer could become a bottleneck when the model's parameter size is small
```

![ptuning2](../resources/img/llms/ptuningv2.png)