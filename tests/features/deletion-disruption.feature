Feature: channel can be deleted

    Scenario: list of two disruptions

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   |cause_id                             |
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        When I get "/disruptions"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 2
        And the field "disruptions.0.id" should be "7ffab232-3d48-4eea-aa2c-22f8680230b6"
        And the field "disruptions.1.id" should be "7ffab230-3d48-4eea-aa2c-22f8680230b6"

        When I delete "/disruptions/7ffab230-3d48-4eea-aa2c-22f8680230b6"
        Then the status code should be "204"


        When I get "/disruptions"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 1
        And the field "disruptions.0.id" should be "7ffab232-3d48-4eea-aa2c-22f8680230b6"

    Scenario: Delete an disruption and impacts

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     | cause_id                             |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff2 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        | severity_id                         |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | 6a826e64-028f-11e4-92d0-090027079ff3 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab234-3d49-4eea-aa2c-22f8680230b6 | 6a826e64-028f-11e4-92d0-090027079ff2 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following ptobject in my database:
            | created_at          | updated_at          | type    | id                                   | uri           | impact_id                           |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | network | 7ffab231-3d48-4eea-aa2c-22f8680230b6 | network:JDR:1 |7ffab232-3d47-4eea-aa2c-22f8680230b6 |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | network | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | network:JDR:2 |7ffab234-3d49-4eea-aa2c-22f8680230b6 |

        Given I have the following applicationperiods in my database:
            | created_at          | updated_at          |id                                   | impact_id                            |start_date                           |end_date    |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 |7ffab232-3d47-4eea-aa2c-22f8680230b1 | 7ffab232-3d47-4eea-aa2c-22f8680230b6 |2014-01-01 16:52:00                  |None        |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 |7ffab234-3d49-4eea-aa2c-22f8680230b2 | 7ffab234-3d49-4eea-aa2c-22f8680230b6 |2014-01-01 16:52:00                  |None        |


        When I delete "/disruptions/6a826e64-028f-11e4-92d0-090027079ff3"
        Then the status code should be "204"

        When I get "/impacts?pt_object_type=network&start_date=2014-01-10T23:52:12Z&end_date=2014-02-20T23:52:12Z"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "objects" should have a size of 1
        And the field "objects.0.id" should be "network:JDR:2"
        And the field "objects.0.impacts" should have a size of 1