Feature: traffic report api

    Scenario: response of traffic report api without "X-Contributors"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I get "/traffic_reports"
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error.message" should be "The parameter X-Contributors does not exist in the header"

    Scenario: response of traffic report api without "X-Coverage"
        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
        I fill in header "X-Contributors" with "contrib1"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I get "/traffic_reports"
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error.message" should be "The parameter X-Coverage does not exist in the header"

    Scenario: response of traffic report api without "Authorization"
        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        When I get "/traffic_reports"
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"
        And the field "error.message" should be "The parameter Authorization does not exist in the header"

    Scenario: response of traffic report api
        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I get "/traffic_reports"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"


    Scenario: impact on network, current_time before publication period
#
#                       |                       01-01-2014                                  02-02-2014
#  publication_period   |                           +-------------------------------------------+
#                       |                                       20-01-2014      30-01-2014
#  application_period   |                                           +------------------+
#                       |
# PtObject: network:JDR:1
#
#  TEST1
#
        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | client_id                            | contributor_id                       |start_publication_date|end_publication_date|
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |2014-01-01 16:52:00|2014-02-02 16:52:00|

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        |severity_id                          |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following ptobject in my database:
            | type      | uri                    | created_at          | updated_at          | id                                         |
            | network   | network:JDR:1          | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 1ffab232-3d48-4eea-aa2c-22f8680230b6       |

        Given I have the relation associate_impact_pt_object in my database:
            | pt_object_id                               | impact_id                            |
            | 1ffab232-3d48-4eea-aa2c-22f8680230b6       | 7ffab232-3d47-4eea-aa2c-22f8680230b6 |


        Given I have the following applicationperiods in my database:
            | created_at          | updated_at          |id                                   | impact_id                            |start_date                           |end_date            |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 |7ffab232-3d47-4eea-aa2c-22f8680230b1 | 7ffab232-3d47-4eea-aa2c-22f8680230b6 |2014-01-20 16:52:00                  |2014-01-30 16:52:00 |

        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I get "/traffic_reports?current_time=2013-12-15T23:52:12Z"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 0
        And the field "traffic_reports" should have a size of 0


    Scenario: impact on network, current_time between start publication period and start application period
#
#                       |                       01-01-2014                                  02-02-2014
#  publication_period   |                           +-------------------------------------------+
#                       |                                       20-01-2014      30-01-2014
#  application_period   |                                           +------------------+
#                       |
# PtObject: network:JDR:1
#
#                                                         TEST2
#
        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | client_id                            | contributor_id                       |start_publication_date|end_publication_date|
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |2014-01-01 16:52:00|2014-02-02 16:52:00|

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        |severity_id                          |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following ptobject in my database:
            | type      | uri                    | created_at          | updated_at          | id                                         |
            | network   | network:JDR:1          | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 1ffab232-3d48-4eea-aa2c-22f8680230b6       |

        Given I have the relation associate_impact_pt_object in my database:
            | pt_object_id                               | impact_id                            |
            | 1ffab232-3d48-4eea-aa2c-22f8680230b6       | 7ffab232-3d47-4eea-aa2c-22f8680230b6 |


        Given I have the following applicationperiods in my database:
            | created_at          | updated_at          |id                                   | impact_id                            |start_date                           |end_date            |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 |7ffab232-3d47-4eea-aa2c-22f8680230b1 | 7ffab232-3d47-4eea-aa2c-22f8680230b6 |2014-01-20 16:52:00                  |2014-01-30 16:52:00 |

        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I get "/traffic_reports?current_time=2014-01-15T23:52:12Z"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 1
        And the field "traffic_reports" should have a size of 1
        And the field "disruptions.0.status" should be "future"
        And the field "disruptions.0.id" should be "7ffab232-3d47-4eea-aa2c-22f8680230b6"
        And the field "disruptions.0.disruption_id" should be "7ffab230-3d48-4eea-aa2c-22f8680230b6"
        And the field "traffic_reports.0.network.id" should be "network:JDR:1"
        And the field "traffic_reports.0.network.name" should be "RATP"
        And the field "traffic_reports.0.network.links" should have a size of 1
        And the field "traffic_reports.0.network.links.0.id" should be "7ffab232-3d47-4eea-aa2c-22f8680230b6"
        And the field "traffic_reports.0.network.links.0.rel" should be "disruptions"


    Scenario: impact on network, current_time between start publication period and end application period
#
#                       |                       01-01-2014                                  02-02-2014
#  publication_period   |                           +-------------------------------------------+
#                       |                                       20-01-2014      30-01-2014
#  application_period   |                                           +------------------+
#                       |
# PtObject: network:JDR:1
#
#                                                                            TEST2
#
        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | client_id                            | contributor_id                       |start_publication_date|end_publication_date|
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |2014-01-01 16:52:00|2014-02-02 16:52:00|

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        |severity_id                          |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following ptobject in my database:
            | type      | uri                    | created_at          | updated_at          | id                                         |
            | network   | network:JDR:1          | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 1ffab232-3d48-4eea-aa2c-22f8680230b6       |

        Given I have the relation associate_impact_pt_object in my database:
            | pt_object_id                               | impact_id                            |
            | 1ffab232-3d48-4eea-aa2c-22f8680230b6       | 7ffab232-3d47-4eea-aa2c-22f8680230b6 |


        Given I have the following applicationperiods in my database:
            | created_at          | updated_at          |id                                   | impact_id                            |start_date                           |end_date            |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 |7ffab232-3d47-4eea-aa2c-22f8680230b1 | 7ffab232-3d47-4eea-aa2c-22f8680230b6 |2014-01-20 16:52:00                  |2014-01-30 16:52:00 |

        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I get "/traffic_reports?current_time=2014-01-23T23:52:12Z"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 1
        And the field "traffic_reports" should have a size of 1
        And the field "disruptions.0.status" should be "active"
        And the field "disruptions.0.id" should be "7ffab232-3d47-4eea-aa2c-22f8680230b6"
        And the field "disruptions.0.disruption_id" should be "7ffab230-3d48-4eea-aa2c-22f8680230b6"
        And the field "traffic_reports.0.network.id" should be "network:JDR:1"
        And the field "traffic_reports.0.network.name" should be "RATP"
        And the field "traffic_reports.0.network.links" should have a size of 1
        And the field "traffic_reports.0.network.links.0.id" should be "7ffab232-3d47-4eea-aa2c-22f8680230b6"
        And the field "traffic_reports.0.network.links.0.rel" should be "disruptions"

    Scenario: impact on network, current_time between end publication period and end application period
#
#                       |                       01-01-2014                                  02-02-2014
#  publication_period   |                           +-------------------------------------------+
#                       |                                       20-01-2014      30-01-2014
#  application_period   |                                           +------------------+
#                       |
# PtObject: network:JDR:1
#
#                                                                                           TEST2
#
        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | client_id                            | contributor_id                       |start_publication_date|end_publication_date|
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |2014-01-01 16:52:00|2014-02-02 16:52:00|

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        |severity_id                          |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following ptobject in my database:
            | type      | uri                    | created_at          | updated_at          | id                                         |
            | network   | network:JDR:1          | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 1ffab232-3d48-4eea-aa2c-22f8680230b6       |

        Given I have the relation associate_impact_pt_object in my database:
            | pt_object_id                               | impact_id                            |
            | 1ffab232-3d48-4eea-aa2c-22f8680230b6       | 7ffab232-3d47-4eea-aa2c-22f8680230b6 |


        Given I have the following applicationperiods in my database:
            | created_at          | updated_at          |id                                   | impact_id                            |start_date                           |end_date            |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 |7ffab232-3d47-4eea-aa2c-22f8680230b1 | 7ffab232-3d47-4eea-aa2c-22f8680230b6 |2014-01-20 16:52:00                  |2014-01-30 16:52:00 |

        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I get "/traffic_reports?current_time=2014-02-01T23:52:12Z"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 1
        And the field "traffic_reports" should have a size of 1
        And the field "disruptions.0.status" should be "past"
        And the field "disruptions.0.id" should be "7ffab232-3d47-4eea-aa2c-22f8680230b6"
        And the field "disruptions.0.disruption_id" should be "7ffab230-3d48-4eea-aa2c-22f8680230b6"
        And the field "traffic_reports.0.network.id" should be "network:JDR:1"
        And the field "traffic_reports.0.network.name" should be "RATP"
        And the field "traffic_reports.0.network.links" should have a size of 1
        And the field "traffic_reports.0.network.links.0.id" should be "7ffab232-3d47-4eea-aa2c-22f8680230b6"
        And the field "traffic_reports.0.network.links.0.rel" should be "disruptions"

    Scenario: impact on network, current_time after end publication period
#
#                       |                       01-01-2014                                  02-02-2014
#  publication_period   |                           +-------------------------------------------+
#                       |                                       20-01-2014      30-01-2014
#  application_period   |                                           +------------------+
#                       |
# PtObject: network:JDR:1
#
#                                                                                                           TEST2
#
        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | client_id                            | contributor_id                       |start_publication_date|end_publication_date|
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |2014-01-01 16:52:00|2014-02-02 16:52:00|

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        |severity_id                          |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following ptobject in my database:
            | type      | uri                    | created_at          | updated_at          | id                                         |
            | network   | network:JDR:1          | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 1ffab232-3d48-4eea-aa2c-22f8680230b6       |

        Given I have the relation associate_impact_pt_object in my database:
            | pt_object_id                               | impact_id                            |
            | 1ffab232-3d48-4eea-aa2c-22f8680230b6       | 7ffab232-3d47-4eea-aa2c-22f8680230b6 |


        Given I have the following applicationperiods in my database:
            | created_at          | updated_at          |id                                   | impact_id                            |start_date                           |end_date            |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 |7ffab232-3d47-4eea-aa2c-22f8680230b1 | 7ffab232-3d47-4eea-aa2c-22f8680230b6 |2014-01-20 16:52:00                  |2014-01-30 16:52:00 |

        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I get "/traffic_reports?current_time=2014-02-15T23:52:12Z"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 0
        And the field "traffic_reports" should have a size of 0