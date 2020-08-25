# Sample App to Demo AWS CDK using Python and AWS Lambda

The sample app is using AWS cloud development kit with python as programming langugage. It creates few demo lambda functions and other supporting components. It is derived using AWS CDK Workshop. 


This project is set up like a standard Python project.  The initialization process also creates
a virtualenv within this project, stored under the .env directory.  To create the virtualenv
it assumes that there is a `python3` executable in your path with access to the `venv` package.
If for any reason the automatic creation of the virtualenv fails, you can create the virtualenv
manually once the init process completes.

## Prerequisites 
Install following 
* python 3
* python3-venv
* pip
* nodejs 
* aws cdk `sudo npm install -g aws-cdk`

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

You can now begin exploring the source code, contained in the hello directory.
There is also a very trivial test included that can be run like this:

```
$ sudo apt install python-pytest
$ pytest
```

To add additional dependencies, for example other CDK libraries, just add to
your requirements.txt file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!



To bootstrap the CDK App, which means that it will create staging bucket to host the code. 
```
cdk bootstrap
```

To synthesize code to cloudformation, use below. If there is no error, then proceed.
```
cdk synth
```

To deploy the cdk sample app:
```
cdk deploy
```


