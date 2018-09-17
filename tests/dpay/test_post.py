from crea.post import Post


def test_post_refresh():
    """ Post should load correctly if passed a dict or string identifier. """
    p1 = Post('https://dsite.io/marketing/@creablog/'
              'marketing-a-crea-ecosystem')
    p2 = Post({
        'author': 'dsiteblog',
        'permlink': 'marketing-a-crea-ecosystem'
    })

    # did post load?
    assert 'json_metadata' in p1 and 'json_metadata' in p2

    # are posts the same
    assert p1.export() == p2.export()
