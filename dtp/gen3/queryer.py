from gen3.submission import Gen3Submission


class Queryer(object):
    """
    Class for querying Gen3.
    Also accepts queries in GraphQL syntax.
    """
    def __init__(self, auth):
        """
        Constructor

        :param auth: Gen3 authentication object created by the Auth class
        :type auth: object
        """
        self._auth = auth
        self._queryer = Gen3Submission(self._auth)

    def graphql_query(self, query_string, variables=None):
        """
        Sending a GraphQL query to Gen3

        :param query_string: query in GraphQL syntax
        :type query_string: string
        :param variables: query variables (optional)
        :type variables: dict
        :return: query response
        :rtype: dict
        """
        response = self._queryer.query(query_string, variables).get("data")

        return response

    def get_programs(self):
        """
        Getting all programs that the user have access to

        :return: List of programs
        :rtype: list
        """
        response = self._queryer.get_programs()

        programs = list()
        for resp in response.get("links"):
            program = resp.split('/')[-1]
            programs.append(program)

        return programs

    def get_projects(self, program):
        """
        Getting the projects by program name

        :param program: Name of a Gen3 program
        :type program: str
        :return: List of projects
        :rtype: list
        """
        response = self._queryer.get_projects(program)

        projects = list()
        for resp in response.get("links"):
            project = resp.split('/')[-1]
            projects.append(project)

        return projects

    def get_node_records(self, node, program, project):
        """
        Getting all the records in a Gen3 node

        :param node: Name of the target node
        :type node: str
        :param program: program name
        :type program: str
        :param project: project name
        :type project: str
        :return: A list of records in dictionary format
        :rtype: list
        """
        response = self._queryer.export_node(program, project, node, "json")
        data = response.get("data")
        return data