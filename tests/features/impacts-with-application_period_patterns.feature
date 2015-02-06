
Feature: Manipulate impacts in a Disruption

    Scenario: Add an impact in a disruption with a application_period pattern having one time_slot

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                             |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     | cause_id                             | client_id                            | contributor_id                       |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I post to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/impacts" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_period_patterns":[{"start_date":"2015-02-01T06:52:00Z","end_date":"2015-02-06T23:52:00Z","weekly_pattern":"1111100","time_slots":[{"begin": "07:45", "end": "09:30"}]}]}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "impact.application_periods" should exist
        And the field "impact.severity.wording" should be "good news"
        And the field "impact.application_periods" should have a size of 5
        And the field "impact.application_periods.0.begin" should be "2015-02-02T07:45:00Z"
        And the field "impact.application_periods.0.end" should be "2015-02-02T09:30:00Z"
        And the field "impact.application_periods.4.begin" should be "2015-02-06T07:45:00Z"
        And the field "impact.application_periods.4.end" should be "2015-02-06T09:30:00Z"

    #If an application_period pattern exist along with application_periods, application_periods is not treated.
    Scenario: Add an impact in a disruption with a application_period pattern having one time_slot and application_periods

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                             |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     | cause_id                             | client_id                            | contributor_id                       |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I post to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/impacts" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_period_patterns":[{"start_date":"2015-02-01T06:52:00Z","end_date":"2015-02-06T23:52:00Z","weekly_pattern":"1111100","time_slots":[{"begin": "07:45", "end": "09:30"}]}], "application_periods": [{"begin": "2014-04-29T16:52:00Z","end": "2014-06-22T02:15:00Z"}]}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "impact.application_periods" should exist
        And the field "impact.severity.wording" should be "good news"
        And the field "impact.application_period_patterns" should have a size of 1
        And the field "impact.application_period_patterns.0.time_slots" should have a size of 1
        And the field "impact.application_periods" should have a size of 5
        And the field "impact.application_periods.0.begin" should be "2015-02-02T07:45:00Z"
        And the field "impact.application_periods.0.end" should be "2015-02-02T09:30:00Z"
        And the field "impact.application_periods.4.begin" should be "2015-02-06T07:45:00Z"
        And the field "impact.application_periods.4.end" should be "2015-02-06T09:30:00Z"

    Scenario: Add an impact in a disruption with an application_periods

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                             |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     | cause_id                             | client_id                            | contributor_id                       |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I post to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/impacts" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_periods": [{"begin": "2015-02-15T08:52:00Z","end": "2015-02-18T23:15:00Z"}]}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "impact.application_periods" should exist
        And the field "impact.severity.wording" should be "good news"
        And the field "impact.application_period_patterns" should have a size of 0
        And the field "impact.application_periods" should have a size of 1
        And the field "impact.application_periods.0.begin" should be "2015-02-15T08:52:00Z"
        And the field "impact.application_periods.0.end" should be "2015-02-18T23:15:00Z"

    Scenario: Add an impact in a disruption with a application_period pattern having two time_slots

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                             |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     | cause_id                             | client_id                            | contributor_id                       |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I post to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/impacts" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_period_patterns":[{"start_date":"2015-02-01T06:52:00Z","end_date":"2015-02-06T23:52:00Z","weekly_pattern":"1111100","time_slots":[{"begin": "07:45", "end": "09:30"}, {"begin": "17:30", "end": "19:30"}]}]}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "impact.application_periods" should exist
        And the field "impact.severity.wording" should be "good news"
        And the field "impact.application_period_patterns" should have a size of 1
        And the field "impact.application_period_patterns.0.time_slots" should have a size of 2
        And the field "impact.application_periods" should have a size of 10
        And the field "impact.application_periods.0.begin" should be "2015-02-02T07:45:00Z"
        And the field "impact.application_periods.0.end" should be "2015-02-02T09:30:00Z"
        And the field "impact.application_periods.1.begin" should be "2015-02-02T17:30:00Z"
        And the field "impact.application_periods.1.end" should be "2015-02-02T19:30:00Z"
        And the field "impact.application_periods.8.begin" should be "2015-02-06T07:45:00Z"
        And the field "impact.application_periods.8.end" should be "2015-02-06T09:30:00Z"
        And the field "impact.application_periods.9.begin" should be "2015-02-06T17:30:00Z"
        And the field "impact.application_periods.9.end" should be "2015-02-06T19:30:00Z"

    Scenario: Add an impact in a disruption with two application_period pattern having one time_slot each

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                             |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     | cause_id                             | client_id                            | contributor_id                       |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I post to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/impacts" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_period_patterns":[{"start_date":"2015-02-01T06:52:00Z","end_date":"2015-02-06T23:52:00Z","weekly_pattern":"1111100", "time_slots":[{"begin": "07:45", "end": "09:30"}]}, {"start_date":"2015-02-01T06:52:00Z","end_date":"2015-02-06T23:52:00Z","weekly_pattern":"0000011", "time_slots":[{"begin": "10:45", "end": "16:30"}]}]}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "impact.application_periods" should exist
        And the field "impact.severity.wording" should be "good news"
        And the field "impact.application_period_patterns" should have a size of 2
        And the field "impact.application_period_patterns.0.time_slots" should have a size of 1
        And the field "impact.application_period_patterns.1.time_slots" should have a size of 1
        And the field "impact.application_periods" should have a size of 6
        And the field "impact.application_periods.0.begin" should be "2015-02-02T07:45:00Z"
        And the field "impact.application_periods.0.end" should be "2015-02-02T09:30:00Z"
        And the field "impact.application_periods.1.begin" should be "2015-02-03T07:45:00Z"
        And the field "impact.application_periods.1.end" should be "2015-02-03T09:30:00Z"
        And the field "impact.application_periods.5.begin" should be "2015-02-01T10:45:00Z"
        And the field "impact.application_periods.5.end" should be "2015-02-01T16:30:00Z"


    Scenario: Update an impact in a disruption having a pattern with two application_period

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                             |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     | cause_id                             | client_id                            | contributor_id                       |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        |severity_id                          |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | a750994c-01fe-11e4-b4fb-080027079ff3 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following pattern in my database:
            | created_at          | updated_at          | id                                   | impact_id                              | weekly_pattern|start_date         |end_date           |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 7ffab200-3d47-4eea-aa2c-22f8680230b6 | 7ffab232-3d47-4eea-aa2c-22f8680230b6   |1111100        |2014-04-06T22:52:12|2014-04-10T22:52:12|
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 7ffab201-3d47-4eea-aa2c-22f8680230b6 | 7ffab232-3d47-4eea-aa2c-22f8680230b6   |0000011        |2014-04-06T22:52:12|2014-04-10T22:52:12|

        Given I have the following timeslot in my database:
            | created_at          | updated_at          | id                                   | pattern_id                          | begin|end  |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 7ffab200-3d47-4eea-aa2c-22f8680230b6 | 7ffab200-3d47-4eea-aa2c-22f8680230b6|07:10 |10:10|
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | 7ffab201-3d47-4eea-aa2c-22f8680230b6 | 7ffab201-3d47-4eea-aa2c-22f8680230b6|07:10 |10:10|

        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"
        When I put to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/impacts/7ffab232-3d47-4eea-aa2c-22f8680230b6" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_periods": [{"begin": "2015-02-05T10:52:00Z","end": "2015-02-07T23:15:00Z"}, {"begin": "2015-02-08T10:52:00Z","end": "2015-02-10T23:15:00Z"}]}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impact.application_periods" should exist
        And the field "impact.severity.wording" should be "good news"
        And the field "impact.application_period_patterns" should have a size of 0
        And the field "impact.application_periods" should have a size of 2
        And the field "impact.application_periods.0.begin" should be "2015-02-05T10:52:00Z"
        And the field "impact.application_periods.0.end" should be "2015-02-07T23:15:00Z"
        And the field "impact.application_periods.1.begin" should be "2015-02-08T10:52:00Z"
        And the field "impact.application_periods.1.end" should be "2015-02-10T23:15:00Z"

    Scenario: Update an impact in a disruption having two application_periods with two patterns

        Given I have the following clients in my database:
            | client_code   | created_at          | updated_at          | id                                   |
            | 5             | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following causes in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |client_id                             |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following severities in my database:
                | wording   | color   | created_at          | updated_at          | is_visible | id                                   |client_id                            |
                | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | True       | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |7ffab229-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following contributors in my database:
            | contributor_code   | created_at          | updated_at          | id                                   |
            | contrib1           | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date     | cause_id                             | client_id                            | contributor_id                       |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | a750994c-01fe-11e4-b4fb-080027079ff3 | 2014-04-15T23:52:12    | 2014-04-19T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |
            | toto      |       | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 6a826e64-028f-11e4-92d0-090027079ff3 | 2014-04-20T23:52:12    | 2014-04-30T23:55:12      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 | 7ffab229-3d48-4eea-aa2c-22f8680230b6 | 7ffab555-3d48-4eea-aa2c-22f8680230b6 |

        Given I have the following impacts in my database:
            | created_at          | updated_at          | status    | id                                   | disruption_id                        |severity_id                          |
            | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d47-4eea-aa2c-22f8680230b6 | a750994c-01fe-11e4-b4fb-080027079ff3 |7ffab232-3d48-4eea-aa2c-22f8680230b6 |


        I fill in header "X-Customer-Id" with "5"
        I fill in header "X-Contributors" with "contrib1"
        I fill in header "X-Coverage" with "jdr"
        I fill in header "Authorization" with "e74598a0-239b-4d9f-92e3-18cfc120672b"

        #Modify impact with two application_periods
        When I put to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/impacts/7ffab232-3d47-4eea-aa2c-22f8680230b6" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_periods": [{"begin": "2015-02-05T10:52:00Z","end": "2015-02-07T23:15:00Z"}, {"begin": "2015-02-08T10:52:00Z","end": "2015-02-10T23:15:00Z"}]}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impact.application_periods" should exist
        And the field "impact.severity.wording" should be "good news"
        And the field "impact.application_period_patterns" should have a size of 0
        And the field "impact.application_periods" should have a size of 2

        #Modify impact with one application_period_pattern and two time slots
        When I put to "/disruptions/a750994c-01fe-11e4-b4fb-080027079ff3/impacts/7ffab232-3d47-4eea-aa2c-22f8680230b6" with:
        """
        {"severity": {"id": "7ffab232-3d48-4eea-aa2c-22f8680230b6"}, "application_period_patterns":[{"start_date":"2015-02-01T06:52:00Z","end_date":"2015-02-06T23:52:00Z","weekly_pattern":"1111100","time_slots":[{"begin": "07:45", "end": "09:30"}, {"begin": "17:30", "end": "19:30"}]}]}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "impact.application_periods" should exist
        And the field "impact.severity.wording" should be "good news"
        And the field "impact.application_period_patterns" should have a size of 1
        And the field "impact.application_period_patterns.0.time_slots" should have a size of 2
        And the field "impact.application_periods" should have a size of 10
        And the field "impact.application_periods.0.begin" should be "2015-02-02T07:45:00Z"
        And the field "impact.application_periods.0.end" should be "2015-02-02T09:30:00Z"
        And the field "impact.application_periods.1.begin" should be "2015-02-02T17:30:00Z"
        And the field "impact.application_periods.1.end" should be "2015-02-02T19:30:00Z"
        And the field "impact.application_periods.8.begin" should be "2015-02-06T07:45:00Z"
        And the field "impact.application_periods.8.end" should be "2015-02-06T09:30:00Z"
        And the field "impact.application_periods.9.begin" should be "2015-02-06T17:30:00Z"
        And the field "impact.application_periods.9.end" should be "2015-02-06T19:30:00Z"
