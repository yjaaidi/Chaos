Feature: Manipulate tags in a Disruption

    Scenario: Display tag in a disruption

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     | cause_id                             |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following tags in my database:
            | name      |  created_at          | updated_at          | is_visible | id                                   |
            | weather   |  2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | strike    |  2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following associatedisruptiontag in my database:
            | disruption_id                                   | tag_id                               | created_at          | updated_at          |id                                   |
            | a750994c-01fe-11e4-b4fb-080027079ff3            | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 |7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | a750994c-01fe-11e4-b4fb-080027079ff3            | 7ffab232-3d48-4eea-aa2c-22f8680230b6 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |

            When I get "/disruptions"
            Then the status code should be "200"
            And the header "Content-Type" should be "application/json"
            And the field "disruptions" should have a size of 1
            And the field "disruptions.0.tags" should have a size of 2
