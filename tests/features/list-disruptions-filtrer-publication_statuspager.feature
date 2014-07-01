Feature: list disruptions with filter publication_status

    Scenario: Filter current_time=2014-05-02T14:00:00Z&publication_status[]='past'
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date |
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |  2014-04-02T14:00:00   | None                 |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |  2014-04-02T14:00:00   | 2014-04-02T19:00:00  |
        When I get "/disruptions?current_time=2014-05-02T14:00:00Z&publication_status[]=past"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 1
        And the field "disruptions.0.publication_period.begin" should be "2014-04-02T14:00:00Z"

    Scenario: Filter current_time=2014-05-02T14:00:00Z&publication_status[]='past'&publication_status[]='ongoing'
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   | start_publication_date | end_publication_date |
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |  2014-04-02T14:00:00   | None                 |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |  2014-04-02T14:00:00   | 2014-04-02T19:00:00  |
        When I get "/disruptions?current_time=2014-05-02T14:00:00Z&publication_status[]=past"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 1
        And the field "disruptions.0.publication_period.begin" should be "2014-04-02T14:00:00Z"