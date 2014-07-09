Feature: Manipulate impacts in a Disruption

    Scenario: Add an impact in a disruption
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        When I post to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/impacts" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "objects": [{"id": "stop_area:RTP:SA:3786125","type": "stop_area"},{"id": "line:RTP:LI:378","type": "line"}]}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "impact.objects" should exist
        And the field "impact.objects.0.id" should be "stop_area:RTP:SA:3786125"
        And the field "impact.objects.0.type" should be "stop_area"
        And the field "impact.severity.id" should exist
        And the field "impact.severity.wording" should be "good news"

    Scenario: Add two impacts via URL in a disruption
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d48-4eea-aa2c-22f8680230b6 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I post to "/disruptions/7ffab232-3d48-4eea-aa2c-22f8680230b6/impacts" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "objects": [{"id": "stop_area:RTP:SA:3786125","type": "stop_area"},{"id": "line:RTP:LI:378","type": "line"}]}
        """
        Given I post to "/disruptions/7ffab232-3d48-4eea-aa2c-22f8680230b6/impacts" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "objects": [{"id": "stop_area:RTP:SA:3786125","type": "stop_area"},{"id": "line:RTP:LI:378","type": "line"}]}
        """
        When I get "/disruptions/7ffab232-3d48-4eea-aa2c-22f8680230b6/impacts"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impacts" should have a size of 2

    Scenario: Get impacts in a disruption
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d48-4eea-aa2c-22f8680230b6 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      |


        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        | severity_id                         |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d49-4eea-aa2c-22f8680230b6 | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |


        When I get "/disruptions/7ffab232-3d48-4eea-aa2c-22f8680230b6/impacts"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impacts" should have a size of 2

    Scenario: Get an impact in a disruption
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d48-4eea-aa2c-22f8680230b6 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        | severity_id                         |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d49-4eea-aa2c-22f8680230b6 | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |


        When I get "/disruptions/7ffab232-3d48-4eea-aa2c-22f8680230b6/impacts"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impacts" should have a size of 2
        And the field "impacts.0.severity.wording" should be "good news"
