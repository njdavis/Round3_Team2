import connexion
from swagger_server.models.error import Error
from swagger_server.models.problem import Problem
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import requests, json
from flask import jsonify
from flask_api import status

storage_url = "http://ec2-35-167-218-237.us-west-2.compute.amazonaws.com:8000/v2/"


"""
    This is the default Problem JSON. It needs to be updated
    as changes are made to API. The default from Swagger can 
    be found in the UI, under Problem - GET
"""
default_problem = {
  "boundary": {
    "boundary_info": {
      "coordinates": [
        {
          "latitude": 0,
          "longitude": 0
        }
      ],
      "shape": "rectangle"
    }
  },
  "goal": {
    "coordinates": {
      "latitude": 0,
      "longitude": 0
    }
  },
  "obstacles": [
    {
      "obstacle_id": 0,
      "obstacle_info": {
        "coordinates": [
          {
            "latitude": 0,
            "longitude": 0
          }
        ],
        "shape": "rectangle"
      }
    }
  ],
  "problem_id": 0,
  "regions": {
    "searched": [
      {
        "id": 0,
        "points": [
          {
            "latitude": 0,
            "longitude": 0
          }
        ],
        "radius": 0
      }
    ],
    "unsearched": {
      "cache": [
        {
          "id": 0,
          "points": [
            {
              "latitude": 0,
              "longitude": 0
            }
          ]
        }
      ],
      "version": 0
    }
  },
  "robots": [
    {
      "coordinates": {
        "latitude": 0,
        "longitude": 0
      },
      "id": 0
    }
  ]
}
def add_problem():
    """
    Creates a new problem and returns a problemID
    

    :rtype: int
    """
    response = requests.post(storage_url, json=default_problem)

    #check if storage comes back okay
    if (response.status_code != 200):
        return jsonify(Error(500, "Error in storage")), HTTP_500_INTERNAL_SERVER_ERROR
    
    #retrieve the problem_id
    json_response = response.json()
    problem_id = json_response['problem_id']
    
    #PUT the default Problem JSON into storage
    params = "id=%s/ver=%s/" % (str(problem_id),"0")
    put_url = storage_url + str(params)
    default_problem['problem_id'] = problem_id
    response = requests.put(put_url, json=default_problem)

    #check if the Problem does exist (It should, but its just for safety's sake)
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    #check that Storage didn't die in some way
    elif (response.status_code != 200):
        return jsonify(Error(response.status_code, response.text)), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #return the default problem so the user knows it has been created
    return jsonify(default_problem)


def delete_problem(problem_id):
    """
    Delete Problem
    This removes the problem by the given ID
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: None
    """

    #make sure ID was valid
    if (problem_id < 0):
        return jsonify(Error(400, "Problem not valid")), status.HTTP_400_BAD_REQUEST
    
    #contact Storage
    params = "id=%s/" % str(problem_id)
    url = storage_url + str(params)
    get_response = requests.delete(url)

    #make sure Problem existed
    if (get_response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if the Storage died
    elif (get_response.status_code != 200):
        return jsonify(Error(response.status_code, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR

    #return response from Storage
    return jsonify({"Message": "Successfully Deleted", "Status": 200})


def get_problem(problem_id):
    """
    Problems
    Returns a specific problem 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Problem
    """

    #make sure ID was valid
    if (problem_id < 0):
        return jsonify(Error(400, "Problem not valid")), status.HTTP_400_BAD_REQUEST

    #contact Storage
    params = "id=%s/" % str(problem_id)
    get_url = storage_url + str(params)
    response = requests.get(get_url)

    #make sure Problem existed
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(response.status_code, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR
    #return response from Storage
    return jsonify(response.json()["body"])
