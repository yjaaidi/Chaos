Feature: Update (put) impacts in a Disruption

    Scenario: Update an impact in a disruption with severity and application_periods in json

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     |cause_ id                             |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        | severity_id                         |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 6a826e64-028f-11e4-92d0-090027079ff3 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d49-4eea-aa2c-22f8680230b6 | 6a826e64-028f-11e4-92d0-090027079ff3 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following ptobject in my database:
            | created_at          | updated_at          | type    | id                                   | uri  | impact_id                           |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | network | 7ffab231-3d48-4eea-aa2c-22f8680230b6 | network:JDR:1 |7ffab232-3d47-4eea-aa2c-22f8680230b6 |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | network | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | network:JDR:2 |7ffab232-3d47-4eea-aa2c-22f8680230b6 |

        When I get "/disruptions/6a826e64-028f-11e4-92d0-090027079ff3/impacts"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impacts" should have a size of 2
        And the field "impacts.0.objects.0.id" should be "network:JDR:1"
        And the field "impacts.0.objects.1.id" should be "network:JDR:2"
        And the field "impacts.0.application_periods" should have a size of 0

        When I put to "/disruptions/6a826e64-028f-11e4-92d0-090027079ff3/impacts/7ffab232-3d47-4eea-aa2c-22f8680230b6" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_periods": [{"begin": "2014-06-01T16:52:00Z","end": "2014-10-22T02:15:00Z"},{"begin": "2014-06-29T16:52:00Z","end": "2014-11-22T02:15:00Z"}]}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impact.objects.0.id" should be "network:JDR:1"
        And the field "impact.objects.1.id" should be "network:JDR:2"
        And the field "impact.application_periods" should have a size of 2
        And the field "impact.application_periods.0.begin" should be "2014-06-01T16:52:00Z"
        And the field "impact.application_periods.0.end" should be "2014-10-22T02:15:00Z"
        And the field "impact.application_periods.1.begin" should be "2014-06-29T16:52:00Z"
        And the field "impact.application_periods.1.end" should be "2014-11-22T02:15:00Z"


    Scenario: Update an impact in a disruption with ptobject/application_periods and without severity in json

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     |cause_ id                             |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        | severity_id                         |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 6a826e64-028f-11e4-92d0-090027079ff3 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d49-4eea-aa2c-22f8680230b6 | 6a826e64-028f-11e4-92d0-090027079ff3 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following ptobject in my database:
            | created_at          | updated_at          | type    | id                                   | uri  | impact_id                           |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | network | 7ffab231-3d48-4eea-aa2c-22f8680230b6 | network:JDR:1 |7ffab232-3d47-4eea-aa2c-22f8680230b6 |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | network | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | network:JDR:2 |7ffab232-3d47-4eea-aa2c-22f8680230b6 |

        When I get "/disruptions/6a826e64-028f-11e4-92d0-090027079ff3/impacts"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impacts" should have a size of 2
        And the field "impacts.0.severity.id" should be "7ffab232-3d48-4eea-aa2c-22f8680230b6"

        When I put to "/disruptions/6a826e64-028f-11e4-92d0-090027079ff3/impacts/7ffab232-3d47-4eea-aa2c-22f8680230b6" with:
        """
        {"objects": [{"id": "network:TAD:CanalTP","type": "network"}, {"id": "network:default_network","type": "network"}], "application_periods": [{"begin": "2014-07-01T16:52:00Z","end": "2014-08-30T02:15:00Z"}]}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impact.objects.0.id" should be "network:JDR:1"
        And the field "impact.objects.1.id" should be "network:JDR:2"
        And the field "impact.objects.2.id" should be "network:TAD:CanalTP"
        And the field "impact.objects.3.id" should be "network:default_network"
        And the field "impact.application_periods" should have a size of 1
        And the field "impact.application_periods.0.begin" should be "2014-07-01T16:52:00Z"
        And the field "impact.application_periods.0.end" should be "2014-08-30T02:15:00Z"
