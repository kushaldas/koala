"""
Core views

"""


class LandingPageView(object):
    """Common view for landing pages

    :ivar display_type: Either 'tableview' or 'gridview'.  Defaults to 'gridview' if unspecified
    :ivar filter_fields: List of models.LandingPageFilter instances for landing page filters (usually at left)
        Leave empty to hide filters on landing page
    :ivar filter_keys: List of strings to pass to client-side filtering engine
        The search box input (usually above the landing page datagrid) will match each property in the list against
        each item in the collection to do the filtering.  See $scope.searchFilterItems in landingpage.js
    :ivar initial_sort_key: The initial sort key used for Angular-based client-side sorting.
        Prefix the key with a '-' to perform a descending sort (e.g. '-launch_time')
    :ivar items: The list of dicts to pass to the JSON renderer to display the collection of items.
    :ivar prefix: The prefix for each landing page, relevant to the section
        For example, prefix = '/instances' for Instances

    """
    def __init__(self, request):
        self.request = request
        self.display_type = self.request.params.get('display', 'gridview')
        self.filter_fields = []
        self.filter_keys = []
        self.initial_sort_key = ''
        self.items = []
        self.prefix = '/'
