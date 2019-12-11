from __future__ import print_function # In python 2.7

from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
import sys
import requests

class Reviews(MethodView):
    def get(self, shop_name):
        """
        GET method for the shops page
        :return: renders the shops.html page on return
        """
        yelp_key = "upTEa2ylIv3izBxQQv2MwPKAa7s95vsgeR7X0Mp4jeIm9cm2SyOCBLvBJ4IhD9a8JzTdPq_UwhaS3nQrcSuQ1qciAWc6rLyU1zouGy1YeQgdIXkOQ1MMwgTfOu7hXXYx"
        r=requests.get("https://api.yelp.com/v3/businesses/search/phone?phone=+19712291617", headers={"Authorization": "Bearer " + yelp_key})
        print(r.text)
        return render_template('reviews.html')

    def post(self):
        """
        POST method for the shops page. Deletes an entry from the db when called.
        :return: renders the shops.html page on return
        """

        return redirect(url_for('reviews'))