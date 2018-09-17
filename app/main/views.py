from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles

@main.route('/')
def index():
    '''
    function that returns the index page
    '''

    # getting source categories
    general_news = get_sources('general')
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    

    title = 'News from your Favorite Sources'
    return render_template('index.html', title = title, general = general_news, business = business_news, entertainment = entertainment_news)


@main.route('/source/<id>')
def source(id):
    '''
    returns source with it's articles
    '''
    article = get_articles(id)
    
    title = f'{id}'

    return render_template('source.html', title = title, article = article)
