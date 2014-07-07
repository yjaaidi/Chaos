Feature: Manipulate impacts in a Disruption

    Scenario: Add an impact in a disruption
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      |

        When I post to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/impacts" with:
        """
        {"objects": [{"id": "stop_area:RTP:SA:3786125","type": "stop_area"},{"id": "line:RTP:LI:378","type": "line"}]}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "impact.status" should be "published"

    Scenario: Add two impacts via URL in a disruption
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d48-4eea-aa2c-22f8680230b6 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      |

        Given I post to "/disruptions/7ffab232-3d48-4eea-aa2c-22f8680230b6/impacts" with:
        """
        {"objects": [{"id": "stop_area:RTP:SA:3786125","type": "stop_area"},{"id": "line:RTP:LI:378","type": "line"}]}
        """
        Given I post to "/disruptions/7ffab232-3d48-4eea-aa2c-22f8680230b6/impacts" with:
        """
        {"objects": [{"id": "stop_area:RTP:SA:3786125","type": "stop_area"},{"id": "line:RTP:LI:378","type": "line"}]}
        """
        When I get "/disruptions/7ffab232-3d48-4eea-aa2c-22f8680230b6/impacts"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impacts" should have a size of 2
        And the field "impacts.0.status" should be "published"


    Scenario: Get impacts in a disruption
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d48-4eea-aa2c-22f8680230b6 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      |

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d49-4eea-aa2c-22f8680230b6 | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |


        When I get "/disruptions/7ffab232-3d48-4eea-aa2c-22f8680230b6/impacts"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impacts" should have a size of 2
        And the field "impacts.0.status" should be "published"

    Scenario: Get an impact in a disruption
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d48-4eea-aa2c-22f8680230b6 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      |

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d49-4eea-aa2c-22f8680230b6 | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |


        When I get "/disruptions/7ffab232-3d48-4eea-aa2c-22f8680230b6/impacts"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impacts" should have a size of 2
