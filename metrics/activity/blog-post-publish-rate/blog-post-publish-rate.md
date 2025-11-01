
# Blog Post Publish Rate

The number of blog posts published over a period of time (weekly).

This is an impactful metric because blog posts as an activity can:
- increase brand awareness
- increase discoverability in organic search (inbound growth)
- deliver value to your ideal customer to solve one of their problems (retention)

You may additionally want to capture **Blog Post Publish Efficiency** which is the publish rate relative to the amount of effort expended (weekly).

## Pre-Conditions

A few things will be needed for successful collection of these metrics.

- you need to have a public blog
- you need to have editorial control to publish at will
- normalize values to 40 hours per work week (5 days) for efficiency calculation

## Measurement

You'll need to gather:
- number of blog posts published between two dates
- amount of time spent producing published posts (estimate)

**Blog Post Production Rate**:
```
number of blog posts published inclusive / number of weeks between first and last publish post
```

**Blog Post Production Rate Efficiency**:
```
number of blog posts published inclusive / hours of effort per post
```

### Example

- Duration: 1 week
- Published posts: 2
- Blog Post Publish Rate: 2.00 (2 / 1)
- Author effort: 5 days
- Blog Post Publish Efficiency: 2.00 (2 / (5 / 5))

### Example

- Duration: 4 weeks
- Published Posts: 9
- Blog Post Publish Rate: 2.25 (9 / 4)
- Total effort by authors (2 authors): 30 days
- Blog Post Publish Efficiency: 1.50 (9 / (30 / 5))

## Analysis

You'll want to combine this activity metric with other outcomes. The objective is to increase the blog publish rate while impacting secondary outcome measures.

- blog attention hours - maintaining or increasing attention hours indicates content is relevant for audience
- blog conversion rate - increasing conversion rate indicates clear CTA

You could also look for trends:
- is blog post publish rate increasing over time
- does blog post publish efficiency vary substantially between two sources of content

### Guardrails

You'll want to combine this activity metric with other outcome metrics that ensure you are achieving a desirable outcome. It would be easy to write shorter articles, low quality articles, or take other short-cuts to increase blog post publish rate at the expense of these desired outcomes.

Good guardrail metrics to compensate:
- blog attention hours - decreasing trend in attention hours indicates content does not engage audience
- blog conversion rate - decreasing conversion rate indicates CTA is unclear

## Obstacles

### What if I don't have a blog?
Free public blogging platforms exist that many teams can leverage. See the DevRel Foundation Tools Catalog for examples. The best time to start a blog if you don't have one for your program is today.

### What If I don't have a blog feed?
If your blog does not support feeds for automatic data collection, you can manually visit the blog and collect the data. Just scroll through the feed and count the number of posts and number of authors for the time period.

### What if I don't have outcome measures?
Collecting activity measures can still be valuable to optimize your workflows around sourcing content.

### What if I don't have enough content being produced?
Many programs will increase their publish rate by sub-contracting out to freelance writers or starting a community writing program.

### What if my team multi-tasks and isn't always focused on content production?
It is common to make a rough approximation. As long as you apply this consistently you can make adjustments in relative terms. You may be able to manage your team in a way to encourage these dedicated periods of time are available.

For example, you may estimate a team of five spends 20% of their time (1 day per week) on blog content production. This is effectively one week of total effort across the team.

### What if my publish rate dropped by half?
It is not unusual for there to be frequent volatility. When there are new product launches or other activities there are many more topics to produce content on. When teams are engaged with technical support, events, or product launches this can  pull attention away from content production for a brief time. The measure is a rate, so extend the period of time to a larger frame to smooth the value out if this becomes a concern. It also gives you framing to share with stakeholders on the impact competing programs may have on your content production deliverables.

### What if other teams contribute content?
It is very common to leverage product, engineering, and other departments in the production of content. The blog post publish rate does not account for whom is creating the content. When calculating blog post publish rate efficiency you would count these other contributors efforts into the cumulative total.

## Automation

Many blogging platforms support RSS or Atom Feeds. In this repository is a python script you can run that will fetch the feed and calculate the number of authors and number of blog posts delivered over a period of time.

```
$ python3 blog-post-publish-rate.py --start 2025-07-01 --end 2025-09-30 --feed https://dev-rel.org/blog/feed.xml
...analyzing 12 weeks
...found 10 articles
blog post publish rate = 0.833
...found 3 authors
...default to 50% time effort
blog post publish efficiency = 0.555

$ python3 blog-post-publish-rate.py --start 2025-07-01 --end 2025-09-30 --effort 45 --feed https://dev-rel.org/blog/feed.xml
blog post publish rate = 0.833
blog post publish efficiency = 1.111 
```
