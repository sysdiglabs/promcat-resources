# Alerts
## etcdMembersDown
etcd cluster: members are down.

## etcdInsufficientMembers
etcd cluster: insufficient members.

## etcdNoLeader
etcd cluster: member has no leader.

## etcdHighNumberOfLeaderChanges
etcd cluster: leader changes within the last 15 minutes. Frequent elections may be a sign of insufficient resources, high network latency, or disruptions by other components and should be investigated.

## etcdHighNumberOfFailedGRPCRequests
etcd cluster: number of requests failed on etcd instance.

## etcdHighNumberOfFailedGRPCRequests
etcd cluster: number of requests failed on etcd instance.

## etcdGRPCRequestsSlow
etcd cluster: gRPC requests to are taking on etcd instance.

## etcdMemberCommunicationSlow
etcd cluster: member communication with is taking on etcd instance.

## etcdHighNumberOfFailedProposals
etcd cluster: proposal failures within the last 30 minutes on etcd instance.

## etcdHighFsyncDurations
etcd cluster: 99th percentile fync durations are on etcd instance.

## etcdHighCommitDurations
etcd cluster: 99th percentile commit durations on etcd instance.

## etcdHighNumberOfFailedHTTPRequests
Number of requests failed on etcd instance

## etcdHighNumberOfFailedHTTPRequests
Number of requests for failed on etcd instance.

## etcdHTTPRequestsSlow
etcd instance HTTP requests to {{ $labels.method }} are slow.
