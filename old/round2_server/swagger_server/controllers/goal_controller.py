import connexion
from swagger_server.models.error import Error
from swagger_server.models.goal import Goal
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import requests, json
from flask import jsonify
from flask_api import status

storage_url = "http://ec2-35-167-218-237.us-west-2.compute.amazonaws.com:8080/v1/"


def get_goal(problem_id):
    """
    Goal Location
    Returns a description of the goal location. 
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Goal
    """
    #check if problem_id is positive
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST
 
    #contact storage
    goal_url = storage_url + str(problem_id)
    response = requests.get(goal_url)

    #check that the Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get the Problem from the response
    problem = response.json()

    reply = {}
    reply["goal"] = problem["goal"]
    reply["version"] = problem["version"]

    #return the Goal from the Problem
    return jsonify(reply)


def update_goal(problem_id, version, goal):
    """
    Update the existing goal value
    
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int
    :param version: The version of the obstacle to be updated.
    :type version: float
    :param goal: Goal object that needs to be updated.
    :type goal: dict | bytes

    :rtype: None
    """
    #check if problem_id is positive 
    if (problem_id < 0):
        return jsonify(Error(400, "Negative Problem_ID")), status.HTTP_400_BAD_REQUEST

    if connexion.request.is_json:
        #get JSON from response
        goal = connexion.request.get_json() 

        #contact Storage
        goal_url = storage_url + str(problem_id)
        response = requests.get(goal_url)
     
        #check that Problem exists
        if (response.status_code == 404):
            return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
        
        #check if Storage died
        elif (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't update goal")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        #get problem from response
        problem = response.json()

        '''
        #check if goal is in valid range
        test_msg = sanitize_goal(goal, problem)
        if (test_msg is not "No error"):
            return jsonify(Error(400, test_msg)), status.HTTP_400_BAD_REQUEST
        '''

        #check that versions are the same
        if (version != problem["version"]):
            message = "Versions numbers do not match. Version should be: " + str(problem["version"])
            return jsonify(Error(409, message)), status.HTTP_409_CONFLICT
        
        #store new Goal coordinates into Goal of Problem
        problem['goal']['coordinates'] = goal['coordinates']

        #update version - incrementing by 0.1 for now because it makes sense
        new_version = problem['version']
        new_version = new_version + 1
        problem["version"] = new_version

        #PUT the new Problem back into Storage
        put_response = requests.put(goal_url, json=problem)
        
        #check if Storage died
        if (response.status_code != 200):
            return jsonify(Error(500, "Storage server error: couldn't update goal")), status.HTTP_500_INTERNAL_SERVER_ERROR
        
        reply = {}
        reply["response"] = put_response.json()
        reply["version"] = problem["version"]

        return jsonify(reply)

    #return an error if input isn't JSON
    return jsonify(Error(415,"Unsupported media type: Please submit data as application/json data")), status.HTTP_415_UNSUPPORTED_MEDIA_TYPE

'''
def sanitize_goal(g, prob):
    coor_count = 0
    if ("coordinates" in g):
        g_coor = g["coordinates"]
        for coor in g_coor:
            if ("latitude" in coor and "longitude" in coor):
                coor_count = coor_count + 1
                g_lat = coor["latitude"]
                g_long = coor["longitude"]
                if (g_lat < -90 or g_lat > 90):
                    return "Invalid latitude: out of range (-90, 90)"
                if (g_long < -180 or g_long > 180):
                    return "Invalid longitude: out of range (-180, 180)"
            else:
                return "Invalid goal: incomplete latitude and longitude pair"
    else: 
        return "Invalid goal: missing coordinates"
    return "No error"
'''