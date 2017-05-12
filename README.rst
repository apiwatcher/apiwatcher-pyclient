Apiwatcher python client
================================

This project aims to be a simple python client for interaction with
Apiwatcher platform.

It solves authentication against platform's ouath2 workflow and thus can be
used as a base for more complex applications.

Installation
=============

Best way is to use *pip*.

.. code-block:: shell

  pip install apiwatcher-pyclient


Usage
======

.. code-block:: python

  from apiwatcher_pyclient.client import Client

  cl = Client()
  cl.authorize_client_credentials(
    "your_client_id", "your_client_secret", scope="apilisk"
  )
  cl.post(
      "/api/projects/xxx/testcase/123456/results",
      {
          "some": "data"
      }
  )
